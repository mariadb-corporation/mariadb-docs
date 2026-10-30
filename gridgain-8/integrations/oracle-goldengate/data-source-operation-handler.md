---
description: >-
  Implement the DataSourceOperationHandler interface to convert GoldenGate source updates into GridGain cache operations, and configure it in Spring XML.
---

# Data Source Operation Handler

The `DataSourceOperationHandler` interface allows you to convert updates from the source database to a cache object and perform cache operations. `DataSourceOperationHandler` interface should be implemented by the user.

{% code title="Java" %}
```java
/**
 * A function that allows applications to perform operations on updates from
 * DataBase and store them to cache. The callback will be invoked on each
 * operation such as insert, update, delete rows, etc.
 */
public interface DataSourceOperationHandler {
    /**
     * Init method. This method will be invoked before the handler starts
     * to receive updates from database.
     *
     * @param ignite Ignite instance.
     */
    public void init(Ignite ignite);

    /**
     * Handle single operation update. This method invoked when
     * {@link GridGainHandler#setMode(String)} in "op" mode.
     *
     * @param dsOp An operation on a data source, containing the current
     *      column values (after the operation occurred) and optionally
     *      the "before" values (before the operation occurred). An operation
     *      can in general be a database operation such as
     *      insert/update/delete or a primary-key update.
     * @param opCtx Operation context contains information about operations.
     */
    public void handleOperation(DsOperation dsOp, OperationContext opCtx);

    /**
     * Handle transaction update. This method invoked when
     * {@link GridGainHandler#setMode(String)} in "tx" mode.
     *
     * @param tx Data source transaction. This object contains info about
     *      whole transaction: changed rows, value, type and etc.
     * @param opCtx Operation context contains information about operations.
     */
    public void handleTransaction(DsTransaction tx, OperationContext opCtx);
}
```
{% endcode %}

The `init()` method is invoked before the handler starts to receive any updates from the database. This is a good place to create caches, check configurations, etc. On each update from the database, GridGain Handler will invoke the `handleOperation()` or `handleTransaction()` method. If GridGain Handler is working in `tx` mode, `handleTransaction` will be invoked. Otherwise, `handleOperation` will be invoked. Implementation of these methods can be used by any Ignite APIs: cache operations, compute, messaging, etc. Here is an example pseudo-code implementation:

{% code title="Java" %}
```java
/**
 * The class transforms updates (id, name and salary columns)
 * to Person cache value and save it to cluster.
 */
public class PersonOperationHandler implements DataSourceOperationHandler {
    /** Column name that contains "Name". */
    public static final String NAME_COL = "name";

    /** Column name that contains "Salary". */
    public static final String SALARY_COL = "salary";

    /** Ignite instance. */
    private Ignite ignite;

    /** Cache person. */
    private IgniteCache<Integer, Person> cache;

    /** {@inheritDoc} */
    @Override public void init(Ignite ignite) {
        this.ignite = ignite;

        cache = ignite.cache("persons");
    }

    /** {@inheritDoc} */
    @Override public void handleOperation(DsOperation dsOp, OperationContext opCtx) {
        handle(dsOp, opCtx);
    }

    /** {@inheritDoc} */
    @Override public void handleTransaction(DsTransaction tx, OperationContext opCtx) {
        try (Transaction igniteTx = ignite.transactions().txStart()) {
            for (DsOperation op : tx.getOperations())
                handle(op, opCtx);

            igniteTx.commit();
        }
    }

    /**
     * The methods convert data from database to {@code Person} object and performs cache operation.
     *
     * @param dsOp An operation on a data source, containing the
     *      current column values (after the operation occurred)
     *      and optionally the "before" values (before the operation occurred).
     *      An operation can in general be a database operation such as
     *      insert/update/delete or a primary-key update.
     * @param opCtx Operation context contains information about operations.
     */
    private void handle(DsOperation dsOp, OperationContext opCtx) {
        TableMetaData tableMeta = opCtx.getMetaData()
            .getTableMetaData(dsOp.getTableName());

        Op op = new Op(dsOp, tableMeta,  opCtx.getConfiguration());

        DsColumn id = op.getColumn(tableMeta
            .getColumnMetaData(new ColumnName("id")).getIndex());

        if (id == null || id.getAfterValue() == null)
            throw new NullPointerException("Column id doesn't exist! Id: " + id + ".");

        int key = Integer.valueOf(id.getBeforeValue());

        if (op.getOpType().isDelete())
            cache.remove(key);
        else if (op.getOpType().isInsert()) {
            String name = null;
            Double salary = null;

            DsColumn nameCol = op.getColumn(tableMeta.getColumnMetaData(new ColumnName(NAME_COL))
                .getIndex());
            DsColumn salaryCol = op.getColumn(tableMeta.getColumnMetaData(new ColumnName(SALARY_COL))
                .getIndex());

            if (!nameCol.isMissing())
                name = nameCol.getAfterValue();

            if (!salaryCol.isMissing())
                salary = Double.valueOf(salaryCol.getAfterValue());

            cache.put(key, new Person(key, name, salary));
        }
        else {
            String name = null;
            Double salary = null;

            DsColumn nameCol = op.getColumn(tableMeta.getColumnMetaData(new ColumnName(NAME_COL))
                .getIndex());
            DsColumn salaryCol = op.getColumn(tableMeta.getColumnMetaData(new ColumnName(SALARY_COL))
                .getIndex());

            if (!nameCol.isMissing())
                name = nameCol.getAfterValue();

            if (!salaryCol.isMissing())
                salary = Double.valueOf(salaryCol.getAfterValue());

            cache.invoke(key, new PersonUpdater(name, salary));
        }
    }

    /**
     * The class updates person.
     */
    public static final class PersonUpdater implements CacheEntryProcessor<Integer, Person, Void> {
        /** */
        private String name;

        /** */
        private Double salary;

        /**
         * @param name Name.
         * @param salary Salary.
         */
        public PersonUpdater(String name, Double salary) {
            this.name = name;
            this.salary = salary;
        }

        /** {@inheritDoc} */
        @Override public Void process(MutableEntry<Integer, Person> entry, Object... arguments)
            throws EntryProcessorException {
            String oldName = entry.getValue() != null ? entry.getValue().name() : null;
            double oldSalary = entry.getValue() != null ? entry.getValue().salary() : 0;

            Person p = new Person(
                entry.getKey(),
                name != null ? name : oldName,
                salary != null ? salary : oldSalary
            );

            entry.setValue(p);

            return null;
        }
    }
}
```
{% endcode %}

The `Handler` should be configured in Spring XML configuration file that is used for starting `GridGain Handler`.

{% code title="XML" %}
```xml
<beans xmlns="http://www.springframework.org/schema/beans"
       xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
       xsi:schemaLocation="http://www.springframework.org/schema/beans
        http://www.springframework.org/schema/beans/spring-beans.xsd">
    <bean id="personOperationHandler" name="personOperationHandler"
      class="org.gridgain.oracle.goldengate.PersonOperationHandler"/>

    <bean class="org.apache.ignite.configuration.IgniteConfiguration">
      ...
    </bean>
</beans>
```
{% endcode %}

You also need to set the `operationHandlerBeanName` parameter for `GridGainHandler` in `dirprm/gridgain.props`.

{% code title="dirprm/gridgain.props" %}
```
gg.handlerlist=gridgain

gg.handler.gridgain.operationHandlerBeanName=personOperationHandler

...
```
{% endcode %}
