#This SQL code was used by the pilot library to extract bookmobile data from their Koha database.

SELECT datetime AS datetime,
       borrowers.city AS community,
       borrowers.zipcode AS zipcode,
       branch AS bookmobile_id,
       itemtype AS "item type",
       ccode AS collection
 FROM statistics
     LEFT JOIN borrowers USING (borrowernumber)
WHERE YEAR(datetime) >= YEAR(DATE_SUB(CURRENT_DATE(),INTERVAL 2 YEAR))
     AND type IN ('issue','renew')
     AND branch IN ('BOOKMOBILE','RURBKMBL')
ORDER BY branch, datetime, itemtype, ccode, borrowers.city 

