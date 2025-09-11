# Introduction & Background

## Introduction

When designing database-based applications, one aspect that might always be considered at first is how you are supposed to maintain these applications; here, we mean maintenance in the sense of application code and database schemas being upgraded and how this can be done with minimum downtime and effort.

This document aims to look at some important aspects of this, from database schema design to application code. Most of these are not strict rules, but rather aspects to consider when working with applications. The document does not cover general application code aspects, only the aspects that deal with the database part of applications.

## Background to Relational Database Applications

Relational database systems, more or less all of them using the SQL query language, have been around since the early 1980s, and things have changed a lot over that time. One aspect that applications using relational databases introduced was the separation of the application, dealing with logic, presentation, user interaction and similar aspects on one hand and the database structure and design on the other.

With relational databases came the relational database modelling and eventually the different normal forms of database design. Much of this has relaxed these days, but there are still things to consider here.

The introduction of logic in the database layer, such as stored procedures, triggers and other aspects, is somewhat blurring the line between code and data, but the general rules still hold.&#x20;
