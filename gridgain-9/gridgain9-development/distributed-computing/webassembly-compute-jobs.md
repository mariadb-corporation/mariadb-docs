---
description: >-
  Run code compiled to WebAssembly on GridGain 9 cluster nodes, including runtime
  configuration, instance caching, and building modules in Rust, Go, WebAssembly
  text format, and Python.
---

# WebAssembly Compute Jobs

You can run your code compiled to WebAssembly with GridGain 9 [Compute API](https://www.gridgain.com/sdk/gridgain9/latest/javadoc/org/apache/ignite/compute/package-summary.html). By default, WASM code will be [compiled into JVM bytecode](https://chicory.dev/docs/usage/runtime-compiler) for faster execution. You can configure this behavior in the compute configuration.

Use [`JobExecutorType.WASM_EMBEDDED`](https://www.gridgain.com/sdk/gridgain9/9.1.9/javadoc/org/apache/ignite/compute/JobExecutorType.html) to load WebAssembly binaries as deployment units and execute the code on cluster nodes.

Before submitting your compute job, ensure that the required code is [deployed](../code-deployment.md) to the nodes where it will execute.

- GridGain 9 uses Chicory 1.5.1 WebAssembly runtime.
- See supported Wasm features here: https://webassembly.org/features/

## Runtime and configuration

By default, WebAssembly code is [compiled to JVM bytecode](https://chicory.dev/docs/usage/runtime-compiler) at runtime for faster execution (Chicory runtime).

You can control this behavior with the `compute.wasm.enableCompiler` setting in the compute configuration.

## Instance Caching

To reduce the startup overhead of module loading and initialization, especially noticeable with some runtimes (for example, Go), GridGain 9 caches WebAssembly instances.

- Instances are cached per deployment unit and file name, avoiding repeated loading and initialization.
- Cached instances are automatically cleared when the corresponding deployment unit is undeployed.

## Configuration Example

Add the following snippet to your `gridgain-config.conf` to define module memory, cache size and TTL parameters.

```javascript
compute {
  wasm {
    enableCompiler = true
    moduleMaxMemory = 8m
    moduleCache {
      enabled = true
      maxSize = 10
      expireAfterAccessSeconds = 5
      expireAfterWriteSeconds = 6
    }
  }
}
```

## WebAssembly Modes

GridGain 9 supports two execution modes for WebAssembly modules:

- *Reactor mode* - Calls specific exported functions from the module.
- *Command mode* - Runs the module as a standalone program that reads input from stdin and writes output to stdout.

The sections below show how you can use these modes, and the recommended platforms for them.

### WebAssembly Reactor Mode

The following sections explain how to build and deploy modules in Rust, Go, and WebAssembly Text Format (Wat).

#### Rust

1. Make sure Rust and Cargo are [installed](https://www.rust-lang.org/tools/install).
2. Install `wasm-pack`:

```bash
cargo install wasm-pack
```

3. Create a new Rust library project:

```bash
cargo new --lib hello-wasm
```

4. Replace the contents of `Cargo.toml` with:

```toml
[package]
name = "hello-wasm"
version = "0.1.0"
edition = "2024"

[lib]
crate-type = ["cdylib", "rlib"]

[dependencies]
wasm-bindgen = "0.2.84"
```

5. Replace the contents of `src/lib.rs` with:

```rust
use wasm_bindgen::prelude::*;

#[wasm_bindgen]
pub fn hello(arg: String) -> String {
    format!("Hello from Rust, {}!", arg)
}
```

6. Build the project with `wasm-pack build`. This will create a `pkg` directory with the compiled Wasm module and JavaScript bindings. We only need one `.wasm` file from this directory: `pkg/hello_wasm_bg.wasm`.
7. Deploy the `.wasm` file as part of a Deployment Unit to your cluster.
8. Run your Rust job using Compute API:

```java
public class ComputeRustJobExample {

    private static final DeploymentUnit DEPLOYMENT_UNIT = new DeploymentUnit("unit-rust", "1.0.0");

    private static final String HELLO_FUNC = "rust_wasm_bindgen_bg.wasm:hello:string:rust_wasm_bindgen";

    private static final JobExecutionOptions JOB_EXECUTION_OPTIONS = JobExecutionOptions.builder()
            .executorType(JobExecutorType.WASM_EMBEDDED)
            .build();

    public static void main(String[] args) throws ExecutionException, InterruptedException {


        System.out.println("\nConnecting to server...");

        try (IgniteClient client = IgniteClient.builder()
                .addresses("127.0.0.1:10800")
                .build()
        ) {

            IgniteCompute compute = client.compute();


            JobDescriptor<String, String> helloDesc = JobDescriptor.<String, String>builder(HELLO_FUNC)
                    .units(DEPLOYMENT_UNIT)
                    .options(JOB_EXECUTION_OPTIONS)
                    .build();

            JobTarget target = JobTarget.anyNode(client.cluster().nodes());

            String helloRes = compute.execute(target, helloDesc, "World");
            System.out.println("Rust job result: " + helloRes);

        }
    }
}
```

For more details, refer to Wasm documentation for Rust:

- [The `wasm-bindgen` Guide](https://wasm-bindgen.github.io/wasm-bindgen/)
- [Compiling from Rust to WebAssembly (MDN)](https://developer.mozilla.org/en-US/docs/WebAssembly/Guides/Rust_to_Wasm)

#### Go

1. Make sure Go is [installed](https://golang.org/doc/install).
2. Create a new directory for your project:

```bash
mkdir hello-wasm && cd hello-wasm
```

3. Initialize a new Go module:

```bash
go mod init hello-wasm
```

4. Create a new file `hello.go` with the following contents:

```go
package main

import (
    "fmt"
    "unsafe"
)

// Store allocated buffers to prevent GC from collecting them.
var buffersSlice = make([][]byte, 0)

func main() {}

//go:wasmexport addOne
func addOne(x int32) int32 {
    return x + 1
}

//go:wasmexport hello
func hello(arg uint64) uint64 {
    if arg == 0 {
        return 0
    }

    argAddr, argLen := unpackPtr(arg)
    argBytes := unsafe.Slice((*byte)(unsafe.Pointer(argAddr)), argLen)
    argStr := string(argBytes)

    resStr := fmt.Sprintf("Hello from Go, %s!", argStr)
    resBytes := []byte(resStr)

    resPtr := uint64(uintptr(unsafe.Pointer(&resBytes[0])))
    resLen := uint64(len(resBytes))

    return packPtr(resLen, resPtr)
}

//go:wasmexport alloc
func alloc(size int32) int32 {
    buffer := make([]byte, size)
    buffersSlice = append(buffersSlice, buffer)
    addr := int32(uintptr(unsafe.Pointer(&buffer[0])))

    return addr
}

//go:wasmexport dealloc
func dealloc(address uint64, size uint32) {
    // No-op.
}

func packPtr(resLen uint64, resPtr uint64) uint64 {
    return (resLen << 32) | resPtr
}

func unpackPtr(arg uint64) (uintptr, uintptr) {
    argAddr := uintptr(arg & 0xFFFFFFFF)
    argLen := uintptr(arg >> 32)
    return argAddr, argLen
}
```

5. Build the project:

```bash
GOOS=wasip1 GOARCH=wasm go build -buildmode=c-shared -o go_hello.wasm
```

6. Deploy the `.wasm` file as part of a Deployment Unit to your cluster.
7. Run your Go job using Compute API:

```java
public class ComputeGoJobExample {

    private static final DeploymentUnit DEPLOYMENT_UNIT = new DeploymentUnit("unit-go", "1.0.0");

    private static final String HELLO_FUNC = "go-test-wasi.wasm:hello:string:go_wasi_reactor";

    private static final JobExecutionOptions JOB_EXECUTION_OPTIONS = JobExecutionOptions.builder()
            .executorType(JobExecutorType.WASM_EMBEDDED)
            .build();

    public static void main(String[] args) throws ExecutionException, InterruptedException {


        System.out.println("\nConnecting to server...");

        try (IgniteClient client = IgniteClient.builder()
                .addresses("127.0.0.1:10800")
                .build()
        ) {

            IgniteCompute compute = client.compute();


            JobDescriptor<String, String> helloDesc = JobDescriptor.<String, String>builder(HELLO_FUNC)
                    .units(DEPLOYMENT_UNIT)
                    .options(JOB_EXECUTION_OPTIONS)
                    .build();

            JobTarget target = JobTarget.anyNode(client.cluster().nodes());

            String helloRes = compute.execute(target, helloDesc, "World");
            System.out.println("Go job result: " + helloRes);

        }
    }
}
```

For more details, refer to Wasm documentation for Go:

- https://go.dev/wiki/WebAssembly

#### WebAssembly Text Format

1. Go to https://webassembly.github.io/wabt/demo/wat2wasm/ and paste the following code into the left pane:

```
(module
    (memory (export "memory") 10)
    (func (export "addOne") (param i32) (result i32)
        local.get 0
        i32.const 1 ;; Value to add
        i32.add
    )
)
```

2. Click the *Download* button.
3. Deploy the downloaded `.wasm` file as part of a Deployment Unit to the cluster.
4. Invoke the functions with Compute API:

```java
public class ComputeWasmJobExample {

    private static final DeploymentUnit DEPLOYMENT_UNIT = new DeploymentUnit("unit-wasm", "1.0.0");

    private static final String HELLO_FUNC = "test-module.wasm:addOne:int32";

    private static final JobExecutionOptions JOB_EXECUTION_OPTIONS = JobExecutionOptions.builder()
            .executorType(JobExecutorType.WASM_EMBEDDED)
            .build();

    public static void main(String[] args) throws ExecutionException, InterruptedException {


        System.out.println("\nConnecting to server...");

        try (IgniteClient client = IgniteClient.builder()
                .addresses("127.0.0.1:10800")
                .build()
        ) {

            IgniteCompute compute = client.compute();


            JobDescriptor<Integer, Integer> helloDesc = JobDescriptor.<Integer, Integer>builder(HELLO_FUNC)
                    .units(DEPLOYMENT_UNIT)
                    .options(JOB_EXECUTION_OPTIONS)
                    .build();

            JobTarget target = JobTarget.anyNode(client.cluster().nodes());

            Integer helloRes = compute.execute(target, helloDesc, 42);
            System.out.println("WASM job result: " + helloRes);

        }
    }
}
```

For more details, refer to Wasm documentation for WebAssembly:

- https://developer.mozilla.org/en-US/docs/WebAssembly/Guides/Understanding_the_text_format

### WebAssembly Command Mode

Some languages and toolchains do not support exported functions. Python with [py2wasm](https://github.com/wasmerio/py2wasm) is one such example.

Command mode provides a simpler interaction pattern via stdin/stdout, but is less efficient, because the module has to be started again on every job execution.

{% hint style="info" %}
only `String` input and output types are supported in command mode.
{% endhint %}

The following section describes how to build and deploy modules with [py2wasm](https://wasmer.io/posts/py2wasm-a-python-to-wasm-compiler) (experimental, requires Python 3.11).

#### Python

1. Install `py2wasm`:

```bash
pip install py2wasm
```

2. Create a Python script, for example:

```python
import sys

def main():
    name = sys.stdin.read().strip()
    if name:
        print(f"Hello, {name}!")
    else:
        print("Hello from Python!")

if __name__ == "__main__":
    main()
```

3. Build the WebAssembly module:

```bash
py2wasm --output hello.wasm hello.py
```

4. Deploy the created `hello.wasm` file as part of a Deployment Unit to the cluster.
5. Run your Python job using Compute API with command mode:

```java
public class ComputePythonJobExample {

    private static final DeploymentUnit DEPLOYMENT_UNIT = new DeploymentUnit("unit-python", "1.0.0");

    public static void main(String[] args) throws ExecutionException, InterruptedException {
        System.out.println("\nConnecting to server...");

        try (IgniteClient client = IgniteClient.builder()
                .addresses("127.0.0.1:10800")
                .build()
        ) {

            IgniteCompute compute = client.compute();

            JobDescriptor<String, String> helloDesc = WasmJobDescriptor.<String, String>commandBuilder("hello.wasm")
                    .units(DEPLOYMENT_UNIT)
                    .build();

            JobTarget target = JobTarget.anyNode(client.cluster().nodes());

            String helloRes = compute.execute(target, helloDesc, "World");
            System.out.println("Python job result: " + helloRes);

        }
    }
}
```

The `commandBuilder()` method automatically configures the job to use command mode execution. The input string is passed to the program's `stdin`, and the output is captured from `stdout`.
