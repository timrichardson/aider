Supported Functions
Zoho Analytics provides you with a variety of inbuilt functions which are predefined mathematical formulas designed to perform specific well-known calculations easily. This section lists the supported inbuilt functions.
Formula Column In-built functions
The following table gives a list of inbuilt functions provided by Zoho Analytics, which can be used to create any formula. The inbuilt formulas are categorized/grouped based on the type of function.
Date Functions | ||
| FUNCTION | DESCRIPTION | EXAMPLE |
| Absolute Month - absmonth(date\_column) | This function will return month and year from a given date value with the format (Month, yyyy). | absmonth('2011/8/7') = August, 2011 |
| Absolute Quarter - absquarter(date\_column) | This function will return Quarter and year from a given date value with the format (Quarter, yyyy). | absquarter('2011/8/7') = Q3, 2011 |
| Absolute Week - absweek(date\_column) | This function will return week and year from a given date value with the format (Week, yyyy). | absweek('06/04/2011') = W14, 2011 |
| Add Date - adddate(date\_column, num\_of\_days) | This function will add the specified number of days(num\_of\_days) to the given date value. | adddate('2011/8/7',10) = 2011/8/1 |
| Add Week addweek(date\_column, num\_of\_weeks) | This function will add the specified number of weeks(num\_of\_weeks) to the given date value. | addweek('2013-08-27',10) = 2013-11-05 |
| Add Month addmonth(date\_column, num\_of\_months) | This function will add the specified number of months(num\_of\_months) to the given date value. | addmonth('2013-08-27',10) = 2014-06-27 |
| Add Quarter addquarter(date\_column, num\_of\_quarters) | This function will add the specified number of quarter(num\_of\_quarter) to the given date value. | addquarter('2013-08-27',10) = 2016-02-27 |
| Add Year addyear(date\_column, num\_of\_years) | This function will add the specified number of year(num\_of\_year) to the given date value. | addyear('2013-08-27',10) = 2023-08-27 |
| Add Time - addtime(data\_column, time) |
This function returns the day by adding the time to the given date column. | addtime ('2002/02/21 18:23:26', '01:20:10') = 2002/02/21 19:43:36 |
| Add Hours addhour(date\_column, num\_of\_hours) | This function returns the day by adding the number of hours to the given date column. | addhour('2013-08-27',10) = 2013-08-27 10:00:00 |
| Add Minutes addminute(date\_column, num\_of\_minutes) | This function returns the day by adding the number of minutes to the given date column. | addminute('2013-08-27',10) = 2013-08-27 00:10:00 |
| Add Seconds addsecond(date\_column, num\_of\_seconds) | This function returns the day by adding the number of seconds to the given date column. | addsecond('2013-08-27',10) = 2013-08-27 00:00:10 |
| Peroid Add period\_add(year\_month, num\_of\_months) | Adds the specified number of months to the period and returns in the format 'yrmth'. | period\_add(198608,6) = 198702 |
| Age Months age\_months(from\_date, to\_date [Optional]) | This function returns the age in months between the two given date columns | age\_months('2013-08-27','2014-06-28') = 10 |
| Age Years age\_years(from\_date, to\_date [Optional]) | This function returns the age in months between the two given date columns | age\_years('2013-08-27','2018-08-03') = 4 |
| Business Completion Day business\_completion\_day(from\_date, num\_of\_days, exclude\_weekends [Optional]) | This function returns the date adding the given number of days excluding the specified weekends. In case weekends is not provided, then Saturday and Sunday are considered as weekends by default. | business\_completion\_day('2018-01-01',10) = 2018-01-15 |
| Business Days business\_days(from\_date, to\_date, exclude\_weekends [Optional]) | This function returns the count of the business days between the two given date columns excluding specified weekends. In case weekends is not provided, then Saturday and Sunday are considered as weekends by default. | business\_days('2018-01-27','2018-08-03') = 134 |
| Business Hours business\_hours(from\_datetime, to\_datetime, work\_start\_time, work\_end\_time, exclude\_weekends [Optional]) | This function returns the count of business hours in the business days between the two given datetime columns. In case weekends is not provided, then Saturday and Sunday are considered as weekends by default. | business\_hours('2018-01-27 10:00:00','2018-08-03 08:00:00','09:00:00','10:00:00','1000001') = 134 |
| Convert String to Date convert\_string\_to\_date(string\_column, date\_format\_of\_the\_value) | Converts the string into date and returns it in the specified format. | convert\_string\_to\_date('24/12/2009', '%d/%m/%Y') = 2009-12-24 |
| Convert to Datetime convert\_to\_datetime(string\_column, date\_format) | This function returns the date-time value by converting the given string. | convert\_to\_datetime('2013 Aug 27','yyyy MMM dd') = 27 Aug, 2013 |
| Convert TZ convert\_tz(date\_column, current\_timezone\_offset, timezone\_to\_be\_converted\_offset) | This function converts the timestamp or a date time value from one time zone to another. The parameters to specify the time zone can be given as Time Zone identifiers, Time Zone Abbreviations or Offsets. To consider the daylight savings during conversion automatically, use Time zone identifiers as parameters. |
|
| Current Date currentdate() | This function updates the current date of the computer or server automatically | currentdate() = 27 Sep, 2024 10:06:18 |
| Current Time current\_time() | This function updates the current time automatically | current\_time() = 27-11-2024, 14:30 |
| Current Timestamp current\_timestamp() | This function updates the current date and time automatically | current\_timestamp()=2024-11-27 14:30:15 |
| Now now() | This function updates the current date and time automatically | now()= 27 Sep, 2024 10:06:18 |
| Today today() | This function updates the current date automatically | today()=27 Sep, 2024 |
| Tomorrow tomorrow() | This function returns the date one day after the current date | tomorrow()=28 Sep,2024 |
| Yesterday yesterday() | This function returns the date for the previous day | yesterday()=26 Sep, 2024 |
| UTC date utc\_date() | Returns the current UTC date. | utc\_date()=27 Sep, 2024 |
| UTC time utc\_time() | Returns the current UTC time. | utc\_time()= 2024-11-27 14:30 |
| UTC date-time utc\_timestamp() | Returns the current UTC date-time value. | utc\_timestamp()= 2024-11-27 14:35:45 |
| Date date(date\_column) | This function returns the date part of the given date and time value. | date('2013-08-07 14:15:16') = 2013-08-07 |
| Date Format date\_format(date\_column, date\_format\_to\_be\_converted) | This function returns the string form of the date for given date format. | date\_format('2008-08-03','%W %M %Y') = Sunday August 2008 |
| Date and Time Diff - dateand timediff(Unit, From Date, To Date[optional] | This function returns the date and time difference between two date columns based on the units specified. The supported units are SECOND, MINUTE, HOUR, DAY, WEEK, MONTH, QUARTER, YEAR. | dateandtimediff(DAY, '2015-01-01', '2015-05-01')=120 The above example returns the difference between the given dates in Days. |
| Date and Time Diff in Duration - datetime\_diff\_in\_duration(date\_column, date\_column [Optional]) | Calculates the date-time difference between the given columns, and returns it as duration. |
|
| Date Diff datediff(date\_column1, date\_column2) | This function returns the difference between the two given date columns. | datediff('2011/8/11','2010/9/11') = 334 |
| Period Diff period\_diff(year\_month, year\_month) | Returns the difference between two periods in months. | period\_diff(198608,198602) = 2 |
| Day - day(date\_column) | This function returns the day of the given date value. | day( '2024/11/27') = Wednesday |
| Day Name dayname(date\_column) | This function returns the name of the weekday for the given date value(Sunday,Monday,...). | dayname('1990-08-07') = Tuesday |
| Day of Week dayofweek(date\_column) | This function will return the number of the day of week of the given date value (Sunday = 1, Monday = 2,...). | dayofweek('2011/9/9') = 6 |
| Day of Month dayofmonth(date\_column) | This function returns the day of the month for the given date value. | dayofmonth('1990-08-07') = 7 |
| Day of Quarter dayofquarter(date\_column) | This function returns the count of days from the start day of the quarter to the given date value. | dayofquarter('2017-08-07') = 38 |
| Day of Year - dayofyear(date\_column) | This function will return the number of the day of the year of the given date value (0 through 365). | dayofyear('2011/9/2') = 245 |
| Days Between days\_between(from\_date, to\_date [Optional]) | This function returns the count of day between the two given date. | days\_between('2018-01-27','2018-08-03') = 188 |
| End date end\_day(date\_units, date\_column) | This function returns the end date for the given date value and date units. | end\_day(month,'2018-08-27') = 2018-08-31 |
| First Date Current Week first\_date\_current\_week(date\_column, week\_start\_day [Optional]) | This function returns the day the current week begins with. You can choose to set the start day of your week in the parameter week\_start\_day by specifying 1 - Sunday, 2- Monday,... 7 - Saturday. By default Sunday is the first day of the week. | first\_date\_current\_week('2013-10-11') = 2013-10-06 |
| From Unixtime - fromunixtime(seconds) | This function returns the unix time for the given seconds value. | fromunixtime('1000') = 1970/01/01 05:46:40 |
| Hour - hour(date\_column) | This function returns the hour of the given date value. | hour('2011/8/7 10:35:23') = 10 |
| Last Day - lastday(date\_column) | This function returns the last day of the month for the given date value. | lastday('2011/9/7') = 2011/9/30 |
| Last N Days last\_nday(date\_column, num\_of\_days) | This function returns a date that is N number of days before the given date. | last\_nday('2018-08-04',15) = 2018-07-21 |
| Last N Months last\_nmonth(date\_column, num\_of\_months) | This function returns the date value for the given year and num\_of\_days values. | last\_nmonth('2018-08-04',15) = 2017-06-04 |
| Next N Days next\_nday(date\_column, num\_of\_days) | Returns a date that is N number of days after the given date. This is calculated from a day after the given date. | next\_nday('2018-08-04',15) = 2018-08-19 |
| Next N Month next\_nmonth(date\_column, num\_of\_months) | Returns a date that is N number of months after the given date. This is calculated from a day after the given date. | next\_nmonth('2018-08-04',15) = 2019-11-04 |
| Next Weekday next\_weekday(date\_column, weekday) | Returns the next date when the specified weekday falls. | next\_weekday('2018-08-01',1) = 2018-08-05 |
| Previous N Day previous\_nday(date\_column, num\_of\_days) | Returns a date that is N number of days before the given date. This is calculated from a day before the given date. | previous\_nday('2018-08-04',15) = 2018-07-20 |
| Previous N Months previous\_nmonth(date\_column, num\_of\_months) | Returns a date that is N number of months before the given date. This is calculated from a day before the given date. | previous\_nmonth('2018-08-04',15) = 2017-05-04 |
| Make Date - makedate(year,num\_of\_days) | This function returns the date value for the given year and number of the day value (0 through 365) | makedate('2011','23') = 2011/1/23 |
| Microsecond microsecond(date\_column) | This function returns the microsecond value from the given date-time argument value. | microsecond('1990-08-07 10:35:23.3427') = 342700 |
| Minute - minute(date\_column) | This function returns the minutes of the given date value. | minute('2011/8/7 10:35:23') = 35 |
| Second - second(date\_column) | This function returns the seconds of the given date/time value. | second('2011/9/7 10:35:23') = 23 |
| Modified Time -modifiedtime() | This function returns the created time of the record (if the record is newly added) or the last modified time of the record. When you apply this function, initially it will return the time at which the formula has been created. Subsequently it will return only the modified time of the record. | |
| Month - month(date\_column) | This function returns the name of the month of the given date value. | month('2011/9/7') = September |
| Month Name monthname(date\_column) | This function returns the name of the month of the given date value. | monthname('2011/9/7') = September |
| Month Number - monthnum(date\_column) | This function returns the number of the month of the given date value. | monthnum('2011/9/7') = 9 |
| Months Between months\_between(from\_date, to\_date [Optional], iswhole\_value [Optional]) | Returns the count of months in fractional value considering 31 days as a month. | months\_between('2013-08-27','2018-08-03',1) = 59 |
| Quarter - quarter(date\_column) | This function returns the quarter of the given date value. | quarter('2011/8/7') = Q3 |
| Quarter Name quartername(date\_column, fiscal\_start\_month [Optional]) | Returns the quarter name of the given date value as a string. | quartername('1990-08-07') = Q3 |
| Quarter Number quarternum(date\_column, fiscal\_start\_month [Optional]) | Returns the quarter of the given date in numeric format. | quarternum('1990-08-07') = 3 |
| Second to Time sec\_to\_time(seconds) | Converts the given number of seconds to time and returns it in hours, minutes and seconds. | sec\_to\_time(86399) = 23:59:59 |
| Second second(date\_column) | Returns the seconds of the given date value. | second('1990-08-07 10:35:23') = 23 |
| Start Date start\_day(date\_units, date\_column) | Returns the start date for given date value and date units. | start\_day(month,'2018-08-27') = 2018-08-01 |
| Sub Date - subdate(date\_column,num\_of\_days) | This function returns the date by subtracting the number of days(num\_of\_days) from the given date value. | subdate('2011/9/15','6') = 1990/9/9 |
| Sub Time - subtime(date\_column,time) | This function returns the date by subtracting the time from the given date with time value. | subtime('2011/02/21 18:23:26','01:20:10') = 2011/02/21 17:03:16 |
| Time time(date\_column) | Returns the time value of the given date-time value argument. | time('2013-08-07 14:15:16') = 14:15:16 |
| Time Format time\_format(time, time\_format\_to\_be\_converted) | Converts the time to the specified format and returns the same. | time\_format('19:30:41.32','%H %h %i %s %f') = 19 07 30 41 320000 |
| Time to Sec time\_to\_sec(date\_column) | Converts the time value in hours and minutes to seconds and returns the same. | time\_to\_sec('2013-08-07 14:15:16') = 51316 |
| Time Diff timediff(to\_date, from\_date) | Returns the difference between two time values passed in the 2 arguments. | timediff('1990-08-17 16:15:14','1990-08-17 14:15:16') = 01:59:58 |
| Timestamp timestamp(date\_column) | Returns the date time expression for a given date value. | timestamp('2008-11-05') = 2008-11-05 00:00:00 |
| Timestamp Add timestampadd(unit, numeric\_column, date\_column) | Returns the date time after adding the specified number of interval. | timestampadd(week,1,'2008-11-05 19:00:00') = 2008-11-12 19:00:00 |
| Timestamp Diff timestampdiff(unit, from\_date, to\_date) | Subtracts the first argument from the second argument and returns the value in the specified unit. | timestampdiff(year,'2002-05-01','2001-01-01') = -1 |
| Timestamp Diff in Duration - timestamp\_diff\_in\_duration(date\_column, date\_column) | Calculates the date time difference between the given timestamp columns and returns it as duration. | timestamp\_diff\_in\_duration('1990-08-17 16:15:14', '1990-08-17 14:15:16') = 0.1:59:58 |
| Unix Timestamp unix\_timestamp(date\_column [Optional]) | Calculates the total number of seconds fromï¿1⁄2 the date '1970-01-01 00:00:00' to the given date-timeï¿1⁄2 and returns the same. | unix\_timestamp('2018-10-10 12:35:45') = 1539174945 |
| Week week(date\_column) | Returns the week of the given date. | week('2008-01-14') = 2 |
| Weekday weekday(date\_column) | Returns weekday of the given date value. | weekday('1990-08-07') = Tuesday |
| Week of Month weekofmonth(date\_column) | Returns the week number of the month for the given date value. | weekofmonth('2008-01-14') = 3 |
| Week of Year weekofyear(date\_column, week\_start\_day [Optional], week\_mode [Optional], fiscal\_start\_month [Optional] | Returns the week number of the given date as numeric value. | weekofyear('1990-08-07') = 32 |
| Year - year(date\_column) | This function returns year from the given date value. | year('2011/9/7') = 2011 |
| Year Week yearweek(date\_column) | Returns the year and week of the given date. | yearweek('2008-01-14') = 200802 |
Duration Functions | ||
| FUNCTION | DESCRIPTION | EXAMPLE |
| Add Duration - add\_duration( duration\_column, duration\_column) | Returns the duration in the default format ('%D.%H:%m:%s') by adding the values in the specified duration columns. |
|
| Add Days to Duration - add\_days\_to\_duration( duration\_column, num\_of\_days) | Returns the duration in the default format ('%D.%H:%m:%s') by adding the number of days to the specified duration column. | add\_days\_to\_duration ('100.11:22:33', 5)= 105.11:22:33 |
| Add Hours to Duration - add\_hours\_to\_duration( duration\_column, num\_of\_hours) | Returns the duration in the default format ('%D.%H:%m:%s') by adding the given number of hours to the specified duration column. | add\_hours\_to\_duration ('100.11:22:33', 5) = 100.16:22:33 |
| Add Minutes to Duration - add\_minutes\_to\_duration( duration\_column, num\_of\_minutes) | Returns the duration in the default format ('%D.%H:%m:%s')by adding the given number of minutes to the specified duration column. | add\_minutes\_to\_duration ('100.11:22:33', 5) = 100.11:27:33 |
| Add Seconds to Duration - add\_seconds\_to\_duration( duration\_column, num\_of\_seconds) | Returns the duration in the default format ('%D.%H:%m:%s') by adding the given number of seconds to the specified duration column. | add\_seconds\_to\_duration ('100.11:22:33', 5) = 100.11:22:38 |
| Add Weeks to Duration -add\_weeks\_to\_duration( duration\_column, num\_of\_weeks) | Returns the duration in the default format ('%D.%H:%m:%s') by adding the given number of weeks to the specified duration column. | add\_weeks\_to\_duration ('100.11:22:33', 5) = 135.11:22:33 |
| Duration to Month - Duration\_to\_months (duration\_column) | Identifies the number of months present in the duration value and return it as a number. | duration\_to\_months ('500.10:35:23') = 16 |
| Duration to Days - duration\_to\_days( duration\_column ) | Identifies the number of days present in the duration argument and returns it as a number. | duration\_to\_days ('500.10:35:23') = 500 |
| Duration to Hours - duration\_to\_hours( duration\_column ) | Identifies the number of hours present in the duration argument and returns it as a number. | duration\_to\_hours ('500.10:35:23') = 12010 |
| Duration to Minutes - duration\_to\_minutes( duration\_column) | Identifies the number of minutes present in the duration argument and returns it as a number. | duration\_to\_minutes ('500.10:35:23') = 720635 |
| Duration to Seconds - duration\_to\_seconds( duration\_column) | Identifies the number of seconds present in the duration argument and returns it as a number. | duration\_to\_seconds( '500.10:35:23') = 43238123 |
| Duration to Weeks - duration\_to\_weeks(duration\_column) | Identifies the number of weeks present in the duration argument and returns it as a number. | duration\_to\_weeks( '500.10:35:23') = 71 |
| Duration to Years - duration\_to\_years(duration\_column) | Identifies the number of years present in the duration argument and returns it as a number. | duration\_to\_years ('500.10:35:23') = 1 |
| Make Duration - make\_duration (num\_of\_years, num\_of\_months, num\_of\_weeks, num\_of\_days, num\_of\_hours, num\_of\_minutes, num\_of\_seconds) | Calculates the duration using the given number of years, months, weeks, days, hours, minutes and seconds. Returns the calculated values in the default format ('%D.%H:%m:%s'). Enter 0 if any of the specified arguments (years, months, weeks, days, hours, minutes, and seconds) does not have a value. | make\_duration ('1', '11', 0, '21', '9', 50,' 5.777') = 721.10:59:23 |
| Subtract Duration - sub\_duration(duration\_column, duration\_column) | Returns the duration in the default format ('%D.%H:%m:%s') by subtracting the values in the specified duration columns. |
|
| Subtract Days from Duration - sub\_days\_from\_duration (duration\_column, num\_of\_days) | Returns the duration in the default format ('%D.%H:%m:%s') by subtracting the given number of days to the specified duration column. |
|
| Subtract Hours from Duration - sub\_hours\_from\_duration (duration\_column, num\_of\_hours) | Returns the duration in the default format ('%D.%H:%m:%s') by subtracting the given number of hours to the specified duration column. |
|
| Subtract Minutes from Duration -sub\_minutes\_from\_duration (duration\_column, num\_of\_minutes) | Returns the duration in the default format ('%D.%H:%m:%s') by subtracting the given number of minutes to the specified duration column. |
|
| Subtract Seconds from Duration -sub\_seconds\_from\_duration (duration\_column, num\_of\_seconds ) | Returns the duration in the default format ('%D.%H:%m:%s') by subtracting the given number of seconds to the specified duration column. |
|
| Subtract Weeks from Duration -sub\_weeks\_from\_duration( duration\_column, num\_of\_weeks) | Returns the duration in the default format ('%D.%H:%m:%s') by subtracting the given number of weeks to the specified duration column. | Sub\_weeks\_from\_durrom\_duration ('200.07:06:06', 5) = 165.07:06:06 |
| To Duration - to\_duration(numeric\_column,[duration\_unit]) | Converts the numeric column into duration data type. The conversion is based on the duration unit specified. By default, the duration unit is taken as second. |
|
| Round Duration - round\_duration(duration\_column,duration\_scale) | Returns the duration value rounded to the given duration scale. |
|
Numeric Functions | ||
| FUNCTION | DESCRIPTION | EXAMPLE |
| Abs - abs(numeric\_column) | This function returns the absolute value (number without sign) of the 'numeric\_column' | pi() = 3.14159265358979 |
| Acos - acos(numeric\_column) | This function returns the arc cosine value of the specified 'numeric\_column'. Returns NULL if the 'numeric\_column' is not in the range-1 to 1. | pow(2,3) = 8 |
| Asin - asin(numeric\_column) | This function returns the arc sine value of the specified 'numeric\_column'. Returns NULL if the 'numeric\_column' is not in the range-1 to 1. | rand() = 0.282164005825449 |
| Atan - atan(numeric\_column) | This function returns the arc tangent value of the specified 'numeric\_column'. | atan(2) = 1.107149 |
| Atan2 - atan2(numeric\_column1, numeric\_column2) | This function returns the arc tangent of the specified columns 'numeric\_column1' / 'numeric\_column2 | atan2(0.8, 0.6) = 0.927295 |
| Ceil - ceil(numeric\_column) | This functions rounds the 'numeric\_column' to the nearest integer which is greater than the 'numeric\_column' | ceil(11.56) = 12 |
| Ceiling ceiling(numeric\_column) | Returns the smallest integer that is greater than or equal to the value of the argument. | ceiling(10.43) = 11 |
| Conv conv(column, current\_base, to\_be\_converted\_base) | Converts the number string from the given base to the required base. | conv('a',16,2) = 1010 |
Convert base convertbase(column, current\_base, to\_be\_converted\_base) | Returns the converted string representation of the number N, from current base to the to be converted base. | convertbase('a',16,2) = 1010 |
| Cos - cos(numeric\_column) | This function returns the cosine value of the specified 'numeric\_column' | cos(0) = 1 |
| Cot - cot(numeric\_column) | This function returns the cotangent value of the specified 'numeric\_column' | cot(0.25) = 3.916317 |
| CRC32 crc32(string\_column) | Returns a 32 bit unsigned output after calculating the cyclic redundency check. | crc32('111') = 1298878781 |
| Degrees - degrees(numeric\_column) | This function returns the angle in Degrees equivalent to the given Radians | degrees(1) = 57.2957795 |
| Exp - exp(numeric\_column) | This function returns the exponential value of the 'numeric\_column' | exp(2) = 7.389056 |
| Floor - floor(numeric\_column) | Rounds the 'numeric\_column' to the nearest integer which is less than the 'numeric\_column' | floor(11.56) = 11 |
| Format format(numeric\_column1, numeric\_column2) | Formats the number by rounding off the number to decimal places specified in the second argument and returns the value. | format(1.0001111,5) = 1.00011 |
| Greatest - greatest(numeric\_column,..., numeric\_column) | Gives the greatest of the given arguments. | greatest(10,20,5) = 20 |
| Least - least(numeric\_column,..., numeric\_column) | Gives the least of the given arguments. | log10(3) = 0.477121 |
| Ln - ln(numeric\_column) | This function returns the natural logarithm of the specified 'numeric\_column' | ln(5) = 1.609438 |
| Log log2(numeric\_column) | Returns the logarithm to the base-2 of the numeric column. | log2(32) = 5 |
| Log10 - log10(numeric\_column) | This function returns the logarithm to the base-10 of the specified 'numeric\_column' | log10(3) = 0.477121 |
| Log2 - log2(numeric\_column) | This function returns the logarithm to the base-2 of the 'numeric\_column | log2(32) = 5 |
| Mod - mod(numeric\_column1, numeric\_column2) | Returns the remainder of the 'numeric\_column1' divided by 'numeric\_column2' | mod(10,3) = 1 |
| OCT oct(column) | Returns the octal value of the number given in the argument. | oct(12) = 14 |
| Pi - pi() | This function returns the numeric value of the pi. | pi() = 3.14159265358979 |
| Power - pow(numeric\_column1, numeric\_column2) | This function returns the value of 'numeric\_column1' raised to the power of 'numeric\_column2' | pow(2,3) = 8 |
| Random - rand() | Returns a random value between 0 and 1. | rand() = 0.9233482386203 |
| Radians - radians(numeric\_column) | Returns the angle in radians equivalent to the given degrees | radians(180) = 3.1415926 |
| Round - round(numeric\_column) | Returns the rounded integer value of the 'numeric\_column'. | round(10.67) = 11 |
| Sign - sign(numeric\_column) | Returns-1, 0, or 1, if the 'numeric\_column' is negative, zero, or positive. | sign(-23) =-1 |
| Sin - sin(numeric\_column) | Returns the sine value of the 'numeric\_column'. | sin(0) = 0 |
| Square - square(numeric\_column) | Returns the square of the specified 'numeric\_column'. | square(10) = 100 |
| Square Root - sqrt(numeric\_column) | Returns the square root of the specified 'numeric\_column'. | sqrt(16) = 4 |
| Tan - tan(numeric\_column) | Returns the tangent value of the specified 'numeric\_column'. | tan(0.5) = 0.546302 |
String Functions | ||
| FUNCTION | DESCRIPTION | EXAMPLE |
| ASCII ascii(string\_column) | Returns the ASCII value of the first character of the given argument. | ascii('abcddb') = 97 |
| Bit Length bit\_length(string\_column) | Returns the value of the length of the string argument in bits. | bit\_length('AA') = 16 |
| Char char(numeric\_column) | Returns a String of characters formed from the code values of the ASCII code given in the arguments. | char(97,98) = ab |
| Char Length char\_length(string\_column) | Returns the number of characters present in the argument. | char\_length('aa1') = 3 |
| Character Length character\_length(string\_column) | Returns the number of characters present in the argument. | character\_length('aa1') = 3 |
| Concat - concat(string\_column,...,string\_column) | Returns the concatenated string of the given arguments. If any one of the argument is null, it returns null. | concat('abcd','ef','db') = abcdefdbd |
| Concat Ignore Null concat\_ignore\_null(string\_column1, string\_column2, ...) | Returns the concatenated string of the given value ignoring null. | concat('abcd','ef',null,'db') = abcdefdb |
| Concat\_WS - concat\_ws(separator,string\_column1 ,....,string\_columnN) | Returns the concatenated string of the given arguments separated by the given separator. If the separator is null, it returns null. | concat\_ws('-','abcd','ef','db') = abcd-ef-db |
| ELT elt(numeric\_column, string\_column1, string\_column2, ...) | Returns the string value available at the index number specified in the first argument. | elt('2','red','rose','is','beautiful') = rose |
| extract\_json extract\_json(json data, path 1, path 2, ...) | Extracts the value from the given JSON based on the key and index provided. | extract\_json(' "Name": "Jane Doe", "Address": ["Los Angeles", "California"1}', 'Address', '[0]') = Los Angeles |
| Field field(string\_column1, string\_column2, ...) | Searches the value in the first argument with all the rest of the arguments and returns the position of the argument where the first match is found. | field('as','has','as','have') = 2 |
| Find in Set find\_in\_set(string\_column, string\_column) | Searches the value in the first argument with the substrings in the second argument, seperated by commas, and returns the position of the substring where the first match is found. | find\_in\_set('10','2,5,8,10') = 4 |
| Hex hex(string\_column) | Returns the corresponding hexadecimal number for each character of the given string. | hex(255) = FF |
| Insert - insert(string\_column, start\_pos, len, new\_string) | Returns the string 'string\_column', with the substring beginning at position 'start\_pos' and 'len' characters long replaced by the string 'new\_string'. 'start\_pos' should be greater than 0. When len is zero, the 'new\_string' is inserted previous to the position 'start\_pos'. | insert('abcddb', 3, 2, 'efgh') = abefghdb |
| Initial Cap initcap(string\_column) | Converts the first character to upper case. | initcap('analytics') = Analytics |
| Index of - indexof(string\_column, sub\_string) | Returns the index of the first occurrence of the string 'sub\_string' in string 'string\_column'. | indexof('abcddb','db') = 5 |
| Instr instr(string\_column, sub\_string) | Returns the position of the first match of second string argument in the first argument. | instr('impossible','possible') = 3 |
| Lcase lcase(string\_column) | Returns the string 'string\_column' with all characters of the given column changed to lowercase. | lcase('ABCd') = abcd |
| Left - left(string\_column, len) | Returns the 'len' number of characters from the left-hand side of the string 'string\_column'. | left('abcdef',3) = abc |
| Length - length(string\_column) | Returns the character length of the string. | length('abcddb') = 6 |
| Locate locate(sub\_string, string\_column, start\_pos) | Returns the index of the first occurence of the string 'sub\_string' in string 'string\_column' starting at the position 'start\_pos'. | locate('db','zohodbdb',6) = 7 |
| Lower lower(string\_column) | Returns the string 'string\_column' with all characters of the given column changed to lowercase. | lower('AbCD') = abcd |
| Lowercase - lowercase(string\_column) | Returns the string 'string\_column' with all characters changed to lowercase. | lowercase('AbCD') = abcd |
| Lpad - lpad(string\_column, len, pad\_string) | Returns the string 'string\_column', left-padded to a length of 'len' characters with the string 'pad\_string'. If length of the string 'string\_column' is greater than 'len', then the first 'len' characters of 'string\_column' is returned. | lpad('DB',5,'a') = aaaDB |
| Ltrim - ltrim(string\_column) | Returns the string 'string\_column' with leading spaces removed. | ltrim(' abcd') = abcd |
| Make Set make\_set(numeric\_column, string\_column, ...) | Returns the corresponding 'set' of arguments from the string arguments that have the bit specified in the first argument. | make\_set(1,'a','b','c') = a |
| Mid mid(string\_column, start\_pos, string\_len) | Return a string from 'string\_column' starting at position 'start\_pos' with a character length of 'len'. | mid('abcddb', 1, 4) = abcd |
| Octet Length octet\_length(string\_column) | Returns the byte length of the string. | octet\_length('abcddb') = 6 |
| ORD ord(string\_column) | If the first character of the string argument is a multi-byte character, then the code calculated from the below formula is returned. 1st byte code + (2nd byte code \* 256) + (3rd byte code \* 256 \* 256) + . . . | ord('2') = 50 |
| Repeat - repeat(string\_column,count) | repeat('Abcd',3) = 'AbcdAbcdAbcd' | |
| Replace - replace(string\_column, from\_string, to\_string) | Returns the string with all occurrences of the string 'from\_str' replaced by the string 'to\_str' | replace('abcdac','ac','db') = abcddb |
| Reverse - reverse(string\_column) | Returns the reverse string of 'string\_column'. | reverse('abcd') = dcba |
| Right - right(string\_column, len) | Returns the 'len' number of characters from the right-hand side of the string 'string\_column' | right('abcdef',4) = cdef |
| Rpad - rpad(string\_column, len, pad\_string) | Returns the string 'string\_column', right-padded to a length of 'len' characters with the string 'pad\_string'. If length of the string 'string\_column' is greater than 'len', then the first 'len' characters of 'string\_column' is returned | rpad('DB',5,'a') = DBaaa |
| Rtrim - rtrim(string\_column) | Returns the string 'string\_column' with trailing spaces removed. | rtrim('abcd ') = abcd |
| Soundex soundex(string\_column) | Returns a soundex string from 'string\_column'. The soundex string is similar for same sounding strings. | soundex('Hello') = H400 |
| Space space(numeric\_column) | The argument value is returned as the number of space characters. | space(6) = ' ' |
| Strcmp - strcmp(string\_column1, string\_column2) | Returns -1 if the 'string\_column1' is smaller than the 'string\_column2', 0 if the two strings are same, and 1 if the 'string\_column1' is greater than the 'string\_column2'. | strcmp('abcd', 'abcde') =-1 |
| Substr substr(string\_column, start\_pos, string\_len [Optional]) | Returns the substring formed by cutting off the string argument passed according to the needs. | substr('abcddb', 2,) = bcddb |
| Substring - substring(string\_column, start\_pos, string\_len) | Returns a substring from 'string\_column'. The substring begins at position 'start\_pos' with the character length of 'string\_len'. | substring('abcddb', 1, 4) = abcd |
| Substring Between substring\_between(string\_column, sub\_string, sub\_string, start\_pos [Optional]) | Returns the characters between the two given substrings in the main string. | substring\_between('abcddb','b','d',1) = c |
| Substring Count substring\_count(string\_column, sub\_string) | Returns the count of substring occurred in the main string. | substring\_count('abcddb','cd') = 1 |
| Substring Index substring\_index(string\_column, delimiter, delimiter\_count) | Returns the substring from string 'string\_column' before count 'delimiter\_count' occurrences of the delimiter 'delimiter'. | substring\_index('how.are.you', '.', 2) = how.are |
| Substring Position substring\_position(string\_column, sub\_string, start\_pos [Optional]) | Returns the position of substring in the main string. | substring\_position('abcddb','cd') = 3 |
| Trim - trim(string\_column) | Returns the string with all spaces removed in prefix and suffix of the string. | trim(' abcd ') = abcd |
| Ucase ucase(string\_column) | Returns the string 'string\_column' with all characters changed to uppercase. | ucase('abcD') = ABCD |
| Unhex unhex(string\_column) | Returns the corresponding character for each pair of hexadecimal digits. | unhex('21') = ! |
| Upper upper(string\_column) | Returns the string 'string\_column' with all characters changed to uppercase. | upper('abcD') = ABCD |
| Uppercase - uppercase(string\_column) | Returns the string 'string\_column' with all characters changed to uppercase. | uppercase('abcD') = ABCD |
Logical Functions | ||
| FUNCTION | DESCRIPTION | EXAMPLE |
| IF - if(expr1,expr2,expr3) | Returns expr2 if expr1 is true else it returns expr3 | if(5> 10,100,3) = 3 |
| If Case if\_case(column, matchExpr1, returnValue1, matchExpr2, returnValue2, ..., elseValue [Optional]) | Returns the 'returnValue' if the given column satisfied with 'matchExpr'. | if\_case('Subject','issue','Issue List',equals('bug'),'Bug List','Support List') = if the 'Subject' column equals issue then it returns 'Issue List' else if 'Subject' column equals 'bug' then it returns 'Bug List' else it returns 'Support List' if\_case('Subject',startswith('issue','bug'),'Issue List',contains('help','Call'),'Call List','Support List') = if the 'Subject' column starts with 'issue' or 'bug' then it returns 'Issue List' else if 'Subject' column contains 'help' or 'Call' then it returns 'Call List' else it returns 'Support List' |
| Ifnull - ifnull(expr1,expr2) | Returns expr1 if expr1 is not null, else it return expr2 | ifnull(null,10) = 10 |
| Is Empty isempty(column) | Returns '1' if the given column does not have any value. Returns '0' if the given column have some value. | isempty(null) = 1 |
| isnull( ) - isnull(expr1) | Returns 1 if expr1 is null, else it returns 0. | isnull(null)- 1 |
General Functions | ||
| FUNCTION | DESCRIPTION | EXAMPLE |
To Email Syntax: to\_email(column) | Converts the plain text column in email format to email datatype. | to\_email(test@abc.com) = test@abc.com |
To Currency Syntax: to\_currency(numeric\_column) | Converts the numeric column to currency data type, | to\_currency(3854) = $3854 |
To Percentage Syntax: to\_percentage(numeric\_column) | Converts the numeric column to percentage datatype. | to\_percentage(83) = 83% to\_percentage(83.54) = 83.54% |
To positive integer Syntax: to\_positive\_integer(column) | Converts the negative values in the numeric column to positive number datatype. | to\_positive\_integer(-40) = 40 |
To decision box Syntax: to\_decision\_box(column) | Converts plain text values and boolean values like yes, no, true, false, on, off, 1 and 0 to decision box (Yes/No) data type. Values other than the above mentioned value will be returned as Null. | to\_decision\_box(yes) = Yes |
Coalesce Syntax: coalesce(null,null,1,...) | Returns 1 if expr1 is null, else it returns 0. | coalesce(null,null,4) = 4 |