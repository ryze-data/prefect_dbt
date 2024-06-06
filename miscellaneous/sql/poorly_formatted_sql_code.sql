select
    expecteddeliverydate
    ,orderdate
    ,lastreceiptdate
    ,pol.lasteditedwhen
    ,validfrom
    validto
from purchasing.purchaseorders as po
inner join purchasing.purchaseorderlines as pol
    on po.purchaseorderid = pol.purchaseorderid
inner join application.people
    on personid = contactpersonid
where lastreceiptdate > '1/1/2016';
