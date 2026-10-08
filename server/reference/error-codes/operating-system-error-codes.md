# Operating System Error Codes

Below is a partial list of more common Linux and Windows operating system error codes.

## Linux Error Codes

The [perror](../../clients-and-utilities/administrative-tools/perror.md) tool can be used to find the error message which is associated with a given error code.

| Number | Error Code      | Description                                     |
| ------ | --------------- | ----------------------------------------------- |
| 1      | EPERM           | Operation not permitted                         |
| 2      | ENOENT          | No such file or directory                       |
| 3      | ESRCH           | No such process                                 |
| 4      | EINTR           | Interrupted system call                         |
| 5      | EIO             | I/O error                                       |
| 6      | ENXIO           | No such device or address                       |
| 7      | E2BIG           | Argument list too long                          |
| 8      | ENOEXEC         | Exec format error                               |
| 9      | EBADF           | Bad file number                                 |
| 10     | ECHILD          | No child processes                              |
| 11     | EAGAIN          | Try again                                       |
| 12     | ENOMEM          | Out of memory                                   |
| 13     | EACCES          | Permission denied                               |
| 14     | EFAULT          | Bad address                                     |
| 15     | ENOTBLK         | Block device required                           |
| 16     | EBUSY           | Device or resource busy                         |
| 17     | EEXIST          | File exists                                     |
| 18     | EXDEV           | Cross-device link                               |
| 19     | ENODEV          | No such device                                  |
| 20     | ENOTDIR         | Not a directory                                 |
| 21     | EISDIR          | Is a directory                                  |
| 22     | EINVAL          | Invalid argument                                |
| 23     | ENFILE          | File table overflow                             |
| 24     | EMFILE          | Too many open files                             |
| 25     | ENOTTY          | Not a typewriter                                |
| 26     | ETXTBSY         | Text file busy                                  |
| 27     | EFBIG           | File too large                                  |
| 28     | ENOSPC          | No space left on device                         |
| 29     | ESPIPE          | Illegal seek                                    |
| 30     | EROFS           | Read-only file system                           |
| 31     | EMLINK          | Too many links                                  |
| 32     | EPIPE           | Broken pipe                                     |
| 33     | EDOM            | Math argument out of domain of func             |
| 34     | ERANGE          | Math result not representable                   |
| 35     | EDEADLK         | Resource deadlock would occur                   |
| 36     | ENAMETOOLONG    | File name too long                              |
| 37     | ENOLCK          | No record locks available                       |
| 38     | ENOSYS          | Function not implemented                        |
| 39     | ENOTEMPTY       | Directory not empty                             |
| 40     | ELOOP           | Too many symbolic links encountered             |
| 42     | ENOMSG          | No message of desired type                      |
| 43     | EIDRM           | Identifier removed                              |
| 44     | ECHRNG          | Channel number out of range                     |
| 45     | EL2NSYNC        | Level 2 not synchronized                        |
| 46     | EL3HLT          | Level 3 halted                                  |
| 47     | EL3RST          | Level 3 reset                                   |
| 48     | ELNRNG          | Link number out of range                        |
| 49     | EUNATCH         | Protocol driver not attached                    |
| 50     | ENOCSI          | No CSI structure available                      |
| 51     | EL2HLT          | Level 2 halted                                  |
| 52     | EBADE           | Invalid exchange                                |
| 53     | EBADR           | Invalid request descriptor                      |
| 54     | EXFULL          | Exchange full                                   |
| 55     | ENOANO          | No anode                                        |
| 56     | EBADRQC         | Invalid request code                            |
| 57     | EBADSLT         | Invalid slot                                    |
| 59     | EBFONT          | Bad font file format                            |
| 60     | ENOSTR          | Device not a stream                             |
| 61     | ENODATA         | No data available                               |
| 62     | ETIME           | Timer expired                                   |
| 63     | ENOSR           | Out of streams resources                        |
| 64     | ENONET          | Machine is not on the network                   |
| 65     | ENOPKG          | Package not installed                           |
| 66     | EREMOTE         | Object is remote                                |
| 67     | ENOLINK         | Link has been severed                           |
| 68     | EADV            | Advertise error                                 |
| 69     | ESRMNT          | Srmount error                                   |
| 70     | ECOMM           | Communication error on send                     |
| 71     | EPROTO          | Protocol error                                  |
| 72     | EMULTIHOP       | Multihop attempted                              |
| 73     | EDOTDOT         | RFS specific error                              |
| 74     | EBADMSG         | Not a data message                              |
| 75     | EOVERFLOW       | Value too large for defined data type           |
| 76     | ENOTUNIQ        | Name not unique on network                      |
| 77     | EBADFD          | File descriptor in bad state                    |
| 78     | EREMCHG         | Remote address changed                          |
| 79     | ELIBACC         | Can not access a needed shared library          |
| 80     | ELIBBAD         | Accessing a corrupted shared library            |
| 81     | ELIBSCN         | .lib section in a.out corrupted                 |
| 82     | ELIBMAX         | Attempting to link in too many shared libraries |
| 83     | ELIBEXEC        | Cannot exec a shared library directly           |
| 84     | EILSEQ          | Illegal byte sequence                           |
| 85     | ERESTART        | Interrupted system call should be restarted     |
| 86     | ESTRPIPE        | Streams pipe error                              |
| 87     | EUSERS          | Too many users                                  |
| 88     | ENOTSOCK        | Socket operation on non-socket                  |
| 89     | EDESTADDRREQ    | Destination address required                    |
| 90     | EMSGSIZE        | Message too long                                |
| 91     | EPROTOTYPE      | Protocol wrong type for socket                  |
| 92     | ENOPROTOOPT     | Protocol not available                          |
| 93     | EPROTONOSUPPORT | Protocol not supported                          |
| 94     | ESOCKTNOSUPPORT | Socket type not supported                       |
| 95     | EOPNOTSUPP      | Operation not supported on transport endpoint   |
| 96     | EPFNOSUPPORT    | Protocol family not supported                   |
| 97     | EAFNOSUPPORT    | Address family not supported by protocol        |
| 98     | EADDRINUSE      | Address already in use                          |
| 99     | EADDRNOTAVAIL   | Cannot assign requested address                 |
| 100    | ENETDOWN        | Network is down                                 |
| 101    | ENETUNREACH     | Network is unreachable                          |
| 102    | ENETRESET       | Network dropped connection because of reset     |
| 103    | ECONNABORTED    | Software caused connection abort                |
| 104    | ECONNRESET      | Connection reset by peer                        |
| 105    | ENOBUFS         | No buffer space available                       |
| 106    | EISCONN         | Transport endpoint is already connected         |
| 107    | ENOTCONN        | Transport endpoint is not connected             |
| 108    | ESHUTDOWN       | Cannot send after transport endpoint shutdown   |
| 109    | ETOOMANYREFS    | Too many references: cannot splice              |
| 110    | ETIMEDOUT       | Connection timed out                            |
| 111    | ECONNREFUSED    | Connection refused                              |
| 112    | EHOSTDOWN       | Host is down                                    |
| 113    | EHOSTUNREACH    | No route to host                                |
| 114    | EALREADY        | Operation already in progress                   |
| 115    | EINPROGRESS     | Operation now in progress                       |
| 116    | ESTALE          | Stale NFS file handle                           |
| 117    | EUCLEAN         | Structure needs cleaning                        |
| 118    | ENOTNAM         | Not a XENIX named type file                     |
| 119    | ENAVAIL         | No XENIX semaphores available                   |
| 120    | EISNAM          | Is a named type file                            |
| 121    | EREMOTEIO       | Remote I/O error                                |
| 122    | EDQUOT          | Quota exceeded                                  |
| 123    | ENOMEDIUM       | No medium found                                 |
| 124    | EMEDIUMTYPE     | Wrong medium type                               |
| 125    | ECANCELED       | Operation Canceled                              |
| 126    | ENOKEY          | Required key not available                      |
| 127    | EKEYEXPIRED     | Key has expired                                 |
| 128    | EKEYREVOKED     | Key has been revoked                            |
| 129    | EKEYREJECTED    | Key was rejected by service                     |
| 130    | EOWNERDEAD      | Owner died                                      |
| 131    | ENOTRECOVERABLE | State not recoverable                           |

## Windows Error Codes

{% hint style="info" %}
For a complete list, see [ms681381.aspx](https://msdn.microsoft.com/en-us/library/ms681381.aspx)
{% endhint %}

| Number | Error Code                       | Description                                                                                  |
| ------ | -------------------------------- | -------------------------------------------------------------------------------------------- |
| 1      | ERROR\_INVALID\_FUNCTION         | Incorrect function.                                                                          |
| 2      | ERROR\_FILE\_NOT\_FOUND          | The system cannot find the file specified.                                                   |
| 3      | ERROR\_PATH\_NOT\_FOUND          | The system cannot find the path specified.                                                   |
| 4      | ERROR\_TOO\_MANY\_OPEN\_FILES    | The system cannot open the file.                                                             |
| 5      | ERROR\_ACCESS\_DENIED            | Access is denied.                                                                            |
| 6      | ERROR\_INVALID\_HANDLE           | The handle is invalid.                                                                       |
| 7      | ERROR\_ARENA\_TRASHED            | The storage control blocks were destroyed.                                                   |
| 8      | ERROR\_NOT\_ENOUGH\_MEMORY       | Not enough storage is available to process this command.                                     |
| 9      | ERROR\_INVALID\_BLOCK            | The storage control block address is invalid.                                                |
| 10     | ERROR\_BAD\_ENVIRONMENT          | The environment is incorrect.                                                                |
| 11     | ERROR\_BAD\_FORMAT               | An attempt was made to load a program with an incorrect format.                              |
| 12     | ERROR\_INVALID\_ACCESS           | The access code is invalid.                                                                  |
| 13     | ERROR\_INVALID\_DATA             | The data is invalid.                                                                         |
| 14     | ERROR\_OUTOFMEMORY               | Not enough storage is available to complete this operation.                                  |
| 15     | ERROR\_INVALID\_DRIVE            | The system cannot find the drive specified.                                                  |
| 16     | ERROR\_CURRENT\_DIRECTORY        | The directory cannot be removed.                                                             |
| 17     | ERROR\_NOT\_SAME\_DEVICE         | The system cannot move the file to a different disk drive.                                   |
| 18     | ERROR\_NO\_MORE\_FILES           | There are no more files.                                                                     |
| 19     | ERROR\_WRITE\_PROTECT            | The media is write protected.                                                                |
| 20     | ERROR\_BAD\_UNIT                 | The system cannot find the device specified.                                                 |
| 21     | ERROR\_NOT\_READY                | The device is not ready.                                                                     |
| 22     | ERROR\_BAD\_COMMAND              | The device does not recognize the command.                                                   |
| 23     | ERROR\_CRC                       | Data error (cyclic redundancy check).                                                        |
| 24     | ERROR\_BAD\_LENGTH               | The program issued a command but the command length is incorrect.                            |
| 25     | ERROR\_SEEK                      | The drive cannot locate a specific area or track on the disk.                                |
| 26     | ERROR\_NOT\_DOS\_DISK            | The specified disk or diskette cannot be accessed.                                           |
| 27     | ERROR\_SECTOR\_NOT\_FOUND        | The drive cannot find the sector requested.                                                  |
| 28     | ERROR\_OUT\_OF\_PAPER            | The printer is out of paper.                                                                 |
| 29     | ERROR\_WRITE\_FAULT              | The system cannot write to the specified device.                                             |
| 30     | ERROR\_READ\_FAULT               | The system cannot read from the specified device.                                            |
| 31     | ERROR\_GEN\_FAILURE              | A device attached to the system is not functioning.                                          |
| 32     | ERROR\_SHARING\_VIOLATION        | The process cannot access the file because it is being used by another process.              |
| 33     | ERROR\_LOCK\_VIOLATION           | The process cannot access the file because another process has locked a portion of the file. |
| 34     | ERROR\_WRONG\_DISK               | The wrong diskette is in the drive. Insert %2 (Volume Serial Number: %3) into drive %1.      |
| 36     | ERROR\_SHARING\_BUFFER\_EXCEEDED | Too many files opened for sharing.                                                           |
| 38     | ERROR\_HANDLE\_EOF               | Reached the end of the file.                                                                 |
| 39     | ERROR\_HANDLE\_DISK\_FULL        | The disk is full.                                                                            |
| 87     | ERROR\_INVALID\_PARAMETER        | The parameter is incorrect.                                                                  |
| 112    | ERROR\_DISK\_FULL                | The disk is full.                                                                            |
| 123    | ERROR\_INVALID\_NAME             | The file name, directory name, or volume label syntax is incorrect.                          |
| 1450   | ERROR\_NO\_SYSTEM\_RESOURCES     | Insufficient system resources exist to complete the requested service.                       |

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
