/*
Name: Snowflake Quick dbt setup

Description: The Purpose of this script is to show an example of what you need to set up to get started with dbt
for exploration purposes. I recommend using rsa keys and mfa to secure your account

helpful links:
https://docs.getdbt.com/reference/database-permissions/snowflake-permissions
https://docs.getdbt.com/docs/cloud/connect-data-platform/connect-snowflake#key-pair
https://docs.snowflake.com/en/user-guide/key-pair-auth
*/

/*
Account level parameters

-- Setup timezone
-- set up query time out
-- setup budget
*/

use role accountadmin;
-- alter account set timezone = 'UTC';
alter account set allow_client_mfa_caching = true;
alter account set statement_timeout_in_seconds = 600;

/*
1 Using USERADMIN, create users
*/

-- create users
use role useradmin;
create role if not exists analyst;

-- it is strongly recommended you enable mfa authentication
create user if not exists devdata
    password = 'UpdatePassword123'
    login_name = 'devdata'
    email = 'InsertEmail'
    must_change_password = true
    comment = 'junior analyst employee unique to every employee accross time';

-- it is strongly recommended you use rsa keys
create user if not exists dbt
    password = 'UpdatePassword123'
    login_name = 'dbt'
    email = 'InsertEmail'
    must_change_password = true
    comment = 'dbt service account';


/*
2 Using SYSADMIN Create snowflake objects
*/
show databases;
use role sysadmin;

-- create warehouse objects
create warehouse if not exists public_xs_wh;
create warehouse if not exists analyst_xs_wh;
create warehouse if not exists dev_analyst_xs_wh;

-- create database and schema objects
create database if not exists raw;
create schema if not exists raw.public;
create database if not exists analytics;
create schema if not exists analytics.public;
create database if not exists dev_analytics;
create schema if not exists dev_analytics.public;


/*
3 Using SECURITYADMIN, grant privileges
*/

-- grant warehouse priviliges
use role securityadmin;
grant usage on warehouse analyst_xs_wh to role analyst;
grant usage on warehouse dev_analyst_xs_wh to role analyst;

-- grant database priviliges

/*
https:--docs.getdbt.com/docs/core/connect-data-platform/connection-profiles
read source data;
create schemas¹
read system tables
*/
-- raw
use role securityadmin;
grant usage on database raw to role analyst;
grant usage on schema raw.public to role analyst;

grant usage on future schemas in database raw to role analyst;
grant select on future tables in database raw to role analyst;
grant select on future views in database raw to role analyst;

-- analytics
use role securityadmin;
grant usage on database analytics to role analyst;
grant usage on schema analytics.public to role analyst;

grant usage on future schemas in database analytics to role analyst;
grant select on future tables in database analytics to role analyst;
grant select on future views in database analytics to role analyst;

-- dev_analytics
use role securityadmin;
grant usage on database dev_analytics to role analyst;
grant usage on schema dev_analytics.public to role analyst;

grant usage on future schemas in database dev_analytics to role analyst;
grant select on future tables in database dev_analytics to role analyst;
grant select on future views in database dev_analytics to role analyst;

/*
3
*/
show roles;
show users;


-- grant users to roles
use role securityadmin;
grant role analyst to role sysadmin; -- or fivetran_user
grant role analyst to user dbt; -- or fivetran_user
grant role analyst to user devdata;
