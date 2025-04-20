Custom Duration Format
Zoho Analytics allows you to use and display the time duration period in various formats. This document explains the various time duration formats available, and how to construct them.
Customizing Duration Format
You can customize the duration format at the Workspace level or at the Table level.
Strings
The following table lists the supported strings to construct the duration format.
| String | Meaning |
| Seconds | |
| %s | Duration in seconds |
| %SSS | Duration in milliseconds |
| %SSSSSS | Duration in microseconds |
| Minutes | |
| %m | Duration in Minutes |
| Hours | |
| %H | Duration in Hours |
| Days | |
| %D | Duration in Days |
Separators
You can use any element as a separator for duration. You can also use a different separator for each element. The following are a few examples of standard patterns.
- 45 days 18 hrs 31 mins 27 secs
- 45 days 18:31:27
- 45 days 18.31.27
- 45.18:31:27
Formats
The following table lists examples of custom duration format.
| Format | Example |
| Single Element | |
| %s | 13456829 |
| %s Sec | 13456829 Sec |
| %SSS | 586 |
| %SSS Millisecond | 586 Millisecond |
| %SSSSSS | 586709 |
| %SSSSSS Microsecond | 586709 Microsecond |
| %m | 86 |
| %m mins | 86 mins |
| %H | 234 |
| %H hrs | 234 hrs |
| %D | 45 |
| %D days | 45 days |
| Seconds And Millisecond or Microsecond | |
| %s.%SSS | 13456829.586 |
| %s.%SSSSSS | 13456829.586709 |
| Hours and Minutes | |
| %H:%m | 234:33 |
| %H.%m | 234.33 |
| %H hrs %m mins | 234 hrs 33 mins |
| %H/%m | 234/33 |
| Hours, Minutes and Seconds | |
| %H:%m:%s | 234:33:44 |
| %H.%m.%s | 234.33.44 |
| %H hrs %m mins %s secs | 234 hrs 33 mins 44 secs |
| %H h %m m %s s | 234 h 33 m 44 s |
| %H/%m/%s | 234/33/44 |
| Days and Hours | |
| %D:%H | 45:18 |
| %D.%H | 45.18 |
| %D Days %H hrs | 45 days 18 hrs |
| %D/%H | 45/18 |
| Days, Hours, Minutes and Seconds | |
| %D:%H:%m:%s | 45:18:31:27 |
| %D.%H.%m.%s | 45.18.31.27 |
| %D days %H hrs %m mins %s secs | 45 days 18 hrs 31 mins 27 secs |
| %D/%H/%m/%s | 45/18/31/27 |
| %D Days %H:%m:%s | 45 days 18:31:27 |
| %D.%H:%m:%s.%SSSSSS | 45.18:31:27.586709 |
| In Swap Position | |
| %m mins %H hrs %D days | 31 mins 18 hrs 45 days |
Format Column
Zoho Analytics auto identifies the data type and its format while importing. Ensure the duration format is displayed as in your source data. You can also change this format when needed.
- Right- click the duration column and select Format Column from the drop- down menu.
- In the Fomat column dialog that opens, Choose the Alignment
- Choose the preferred format from the list or enter the duration format in the given field.
Edit Duration Values
Follow the below steps to edit a column that has duration values:
- Double - click on any cell that contains duration data.
- Click the Duration icon and modify the values as needed. You can also view the full duration value, irrespective of the format chosen.