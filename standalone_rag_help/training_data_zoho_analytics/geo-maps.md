Geo Data Visualization (Map Charts) for Zoho Analytics
A map chart is a map of a world, continent, or country, with the data values assigned to specific regions through chart visualizations. These map charts are also called as Geovisualization. It refers to the analysis of geospatial data through the use of interactive visualization.
Geo Charts Basic
- Who can create a map chart and what do you need?
- What kind of data can be visualized in map charts?
- Will Zoho Analytics automatically identify the Geodata?
- How do I set the data type of a column as Geo?
- I get an error message "Invalid GEO LOCATION" while importing geodata into Zoho Analytics. How do I resolve them?
- I have Latitude and Longitude specific information in my dataset, can I create a map chart using that?
- I have postal zipcode in my dataset, can I create a map chart using that?
- I have IATA airport code in my dataset, can I create a map chart using that?
- What are unresolved locations and from where do I access the list?
- I have created a map chart but there are some unresolved locations, how do I resolve them?
Creating Geo Charts
- What are the supported Map chart types?
- How do I create a map chart?
- How do I create a Geo Heat Map chart?
- Can I create a map chart for specific countries alone and hide the rest of the map?
- How do I create a map chart using the latitude and longitude columns?
- How do I create a map chart using the IATA airport code columns?
- I have a column whose data-type I do not want to change to "Geo". Can I still create a map chart using it?
- I have a few location-specific data imported into Zoho Analytics. However, I do not find the map charts option in my chart designer while creating reports using this data. What could be the possible reason?
- What are the interaction options available on map charts?
Creating Spatial Data Geo Charts
- What is a spatial data file?
- How do I analyze spatial data files in Zoho Analytics?
- What are the supported geometry data types in Zoho Analytics?
- What are the supported file formats of spatial data in Zoho Analytics?
- Who can create a spatial map chart?
- What is a geometry column in a spatial data table?
- Will Zoho Analytics automatically identify the geometry column?
- What is a custom-geo column in a spatial data table?
- Can I import spatial data into an existing table?
- Are there any restrictions/limitations while importing spatial data files into Zoho Analytics?
Creating Geo Charts with Image Background
- What are geo charts with image background?
- What type of data values can be visualized in geo charts with image backgrounds?
- What are the image types supported in geo charts with image background?
- How to create geo charts with image background for coordinate values?
- I have image coordinate values in my data table, but I do not see the Map charts option in Zoho Analytics. Why?
Customizing Geo Charts
- How do I customize the map chart settings?
- How do I customize the map chart Theme?
- Can I create the map chart over the satellite map?
- Can I use a continuous color range legend for map chart?
- Can I customize the default home screen of the map chart?
- How do I customize the marker used in a map-scatter chart?
- How do I customize the color of the charts plotted in the map?
- How do I customize the legend settings in a map chart?
Geo Charts Basic
1. Who can create a map chart and what do you need?
Any Zoho Analytics user who wishes to visualize geographical data can create this chart. You will need a location-specific data column to create this chart.
2. What kind of data can be visualized in map charts?
If your dataset contains location information (say, country, county, city etc) then you can use map charts to visualize your data. Zoho Analytics will auto-identify the columns types while importing and set the corresponding Geo data type. Currently, Zoho Analytics can auto-identify 5 types of Geodata.
- Continent - If your column contains the names of the continents or their codes.
- Country - If your column contains the names of countries or their codes (alpha 2-code and alpha 3-code).
- County - If your column contains the names of counties .
- State/Province - If your column contains the names of states/provinces.
- City - If your column contains the names of cities.
- Zip Code - If your column contains postal code of locations.
- Latitude and Longitude - If your column contains latitude and longitude of locations Click here to know about the supported DMS formats.
- Airport - If your column contains airport IATA code.
- Geometry column and Custom Geometry column - If your column contain geometric data for spatial table.
3. Will Zoho Analytics automatically identify the Geodata?
Yes. When you import data into Zoho Analytics if your dataset contains a geographical column (continent, country, county, state or city ) it will be automatically set to the corresponding Geo data type.
Names or Codes: If the data contains names of countries, Alpha-2 and Alpha-3 country codes, names of continents, states, cities, districts, counties, or provinces, then the data type of those columns will be automatically identified as geo location.
Latitude and Longitude: If the latitude/longitude column is in Degrees Minutes Seconds (DMS) format, then Zoho Analytics will automatically identify the data type of the column as latitude or longitude; otherwise it will be identified as decimal number.You can change the data type in the Data Preview section during import or from the table using Change Data Type option.
Airport: If the data contains IATA's unique 3-letter code, then the data type of the column will be automatically identified as Airport.
Postal Code: If the data contains postal code information it will be identified as a positive number. You can change the data type in the Data Preview section during import or from the table using Change DataType option.
Note:
Zoho Analytics will not identify the columns as geo location:
- If there are spelling errors in the location's name. In this case, you can use the Find and Replace option or use Zoho DataPrep during import to correct the misspelt locations.
- If the latitude or longitude columns have any other DMS format other than the supported formats, the data type of those columns will not be automatically identified.
4. How do I set the data type of a column as Geo?
When you import the data into Zoho Analytics if your dataset contains a geographical column (continent, country, state, city or district) it will be automatically set to the corresponding Geo data type. If your existing table contains a geographical column and you wish to change the data type,
- Right-click the column header and select Change Data Type
- Select the correct Geo data type from the Data Type drop-down
- Click OK
5. I get an error message "Invalid GEO LOCATION" while importing geodata into Zoho Analytics. How do I resolve them?
This error message will be displayed when your geo data contains duplicated/ambiguous location names, misspelled locations, colloquial names for places, etc. You can resolve these issues from the imported table or from the geo map chart. Click here to learn more.
6. I have Latitude and Longitude specific information in my dataset, can I create a map chart using that?
Yes, you can. To create map chart using latitude and longitudes, you need both latitude and longitude data as different columns in your dataset and set the data type of the columns to Latitude/Longitude.
Follow the below steps to change the data type of your column.
- Right-click the column name and select Change Data Type.
- Select the Latitude/Longitude from the drop-down.
- Click OK.
Note: Make sure that the data type is changed to Latitude or Longitude to use the format specific to the latitude and longitude columns.
Follow the below steps to format the column
- Right-click the Latitude or Longitude column and select Format Column from the drop-down menu.
- In the Format Column dialog that opens,Specify the Alignment
- Choose the preferred format from the Display Format drop-down.Supported formats are
- Decimal
- (+/-) 12.3456789
- Degrees Minutes Seconds (DMS)
- (+/-) 12° 34' 56"
- 12° 34' 56" (N|S|E|W)
- (+/-) 12d 34m 56s
- 12d 34m 56s (N|S|E|W)
- (+/-) 12.3456°
- 12.3456° (N|S|E|W)
- Decimal
- Click OK
Once you have set the data type as latitude and longitude. You can create reports using this.
7. I have postal zip code in my dataset, can I create a map chart using that?
Yes, you can. To create a chart using this you need to change the data type of the column to Zip code.
Follow the below steps to change the data type of your column to Zip Code.
- Right-click the column name and select Change Data Type.
- Select the Zip Code from the drop-down.
- Click OK.
Once you have set the data type as Zip Code. You can create reports using this.
8. I have airport IATA code in my dataset, can I create a map chart using that?
Yes, you can. Zoho Analytics will automatically identify your data as IATA code. In case it is not identified, then you need to change the data type of the column to Airport.
Follow the below steps to change the data type of your column to Airport.
- Right-click the column name and select Change Data Type.
- Select the Airport from the drop-down.
- Click OK.
Once you have set the data type as Airport. You can create reports using this.
9. What are unresolved locations and from where do I access the list?
When you plot a map chart, sometimes Zoho Analytics might not plot all the data points in the map. This could be due to issues in resolving the geolocation such as duplicated/ambiguous location names, misspelled locations, the colloquial name for places etc.
When Zoho Analytics is not able to identify a location, it lists it as an Unresolved Location(s) for the user to rectify the issue. You can find the list of unresolved locations by:
From a Table
Right-clicking the geo column from your table and select Set Geo Hierarchy from the drop-down.
From a Map Chart
Clicking the Unresolved Location(s) icon that appears in the Map toolbar when you mouse over the chart in the Edit Mode.
10. I have created a map chart but there are some unresolved locations, how do I resolve them?
Unresolved locations as mentioned in the previous question are geo locations (places) that Zoho Analytics is not able to identify. You can help Zoho Analytics to resolve them, by providing the required/missing information, as described in the below steps.
Resolving through Geo Column Mapping
Mapping it to a country column: This will allow Zoho Analytics to identify the country in which the unresolved place is located and plot it appropriately. If you have a country column in your data set, you can map it to resolve the unresolved locations.
In case you do not have a country column, but all the state/cities belong to a single country, you can use Provide the Location option and enter the name of the country.
Mapping it to a state column: This is in addition to mapping the location to a country column. If your dataset contains a state column further mapping it to a state column will help Zoho Analytics identify the state in which the unresolved location is located.
In case you do not have a state column, but all the cities belong to a single state, you can enter the name of the state by selecting Provide the Location option as described above in the case of a country.
Note: Alternatively, as mentioned in the previous question, you can resolve these issues from the parent table as well.
Correcting Misspelt Locations
Zoho Analytics will not be able to identify the location if the spelling of the location is not correct. For example., Hong Kong spelled as Hongkong or Brooklyn being spelled as Broklyn.
In this case, we recommend you to correct the spelling either in the original data and then import it into Zoho Analytics or make the necessary corrections in the Zoho Analytics table.
Plotting the Latitude and Longitude
You can also resolve the issues by specifying the latitude and the longitude values of the corresponding location in the unresolved locations page.
Pick the Location
You can also pick the location by clicking the Pick Location link. Search the location in the map using the given search field. Place the picker in the correct geolocation in the map and click Apply. The latitude and the longitude values for the selected location will be auto-filled in the respective fields.
Creating Geo Charts
1. What are the supported map chart types?
Currently, Zoho Analytics supports the following types of map charts,
- Map Scatter
- Map Bubble
- Map Pie
- Map Bubble Pie
- Map Filled
- Geo Heat Map
Zoho Analytics will auto-identify the appropriate Geo Map type from the columns used in the chart. You can also choose to change the chart type using the Other Charts option.
2. How do I create a map chart?
You can create a map chart by dragging and dropping a geographical column (a column of type "Geo") into the X- Axis shelf and the required columns in other shelves. The below animation shows how to create a map chart.
3. How do I create a Geo Heat Map chart?
Geo Heat Map chart displays data in a geo-map, color coded based on the density of points in a particular area. This enables you to identify the geographical location with a high contribution of your data such as region with most deforestation and climatic changes, where your traffic sources are from, region with most sales, etc.,
The below animation shows how to create a Geo Heat Map chart illustrating regions with high level of earthquakes in North America based on its magnitude.
4. Can I create a map chart for specific countries alone and hide the rest of the map?
Yes, you can create a map chart for specific countries alone by selecting the country-specific map. You can change the map type from the Maps tab of the Settings page.
The below animation shows you how to create a chart over specific countries.
- This is a fixed map and only the countries and their respective state information will be visible. In case of the live map, you can zoom in till the street level.
- In this mode, you can plot the chart for both across the world or on specific countries.
5. How do I create a map chart using the latitude and longitude columns?
To create a map chart using the latitude and longitude information, you need to ensure that the data type of the column is set to Latitude and Longitude. Refer to this section to learn how.
The below animation shows you how to create a chart using Latitude and Longitude data. In this chart, we have plotted the total profit gained in a location grouped by product category.
6. How do I create a map chart using the Airport information (IATA Code)?
To create a map chart using the airport information (IATA code), you need to ensure that the data type of the column is set Airport. Refer to this section to learn how.
The below animation shows how to create a chart using Airport data. This chart plots the busiest airports in the US, based on the number of flights per day.
7. I have a column whose data-type I do not want to change to "Geo". Can I still create a map chart using it?
Yes, you can do it using the Treat as Geo option in the chart designer. When you use this option data type of the column used in creating the report will be considered as a Geo Data Type only for that particular report.
In the below animation, the column 'State' is of string data type. We have created a map chart using this column by using the option 'Treat as Geo'.
8. I have a few location-specific data imported into Zoho Analytics. However, I do not find the map charts option in my chart designer while creating reports using this data. What could be the possible reason?
You will not find the map charts option while creating reports with location-specific points if your imported location-specific data is set as a Text data type. Please change the data type of the location-specific data to Geo Location data type. To change the data type of a column, please follow the below steps:
- Right-click the required column and select Change Data Type from the drop-down.
- In the Change Data Type pop-up menu, choose the required Geo-Location data type from the list of options available.
Your data type will be successfully updated. You can now create map charts over this data.
9. What are the interaction options available on map charts?
Zoho Analytics provides an immersive geo map visualization with its wide range of interaction options. You can interact with the overall map chart using the map toolbar options that appear on the left corner of the map. Regular chart marker and legend specific interactions are also available, providing an immersive geo map visualization experience.
Interactions using the Map Toolbar
- Search - Allows you to search the location
- Home - Fits the map to screen
- Grab Area - Zooms the selected area
- Zoom in - Zoom to view till the street
- Zoom out
Chart Interactions
You can use all the regular interaction options over the chart marker & legend that are listed below:
Creating Spatial Data Geo Charts
1. What is a spatial data file?
A spatial data file contains the location, size, and shape of a geometric value. Using a spatial data file, you will be able to plot custom locations/shapes while creating geo-map charts in Zoho Analytics.
2. How do I analyze spatial data files in Zoho Analytics?
With data from Spatial files, you can create geo-map charts. These files contain location-specific points in the data, thereby helping us plot the data to the correct location in the map charts.
Let us see how to analyze spatial data file with the help of the video below.
3. What are the supported geometry data types in Zoho Analytics?
The supported geometry data types in Zoho Analytics are:
- Point
- Polygon
- Multi-Polygon
4. What are the supported file formats of spatial data in Zoho Analytics?
The supported file formats of spatial data in Zoho Analytics are:
- Shapefiles (Zip format with all the dependent files)
- TopoJSON files
- GeoJSON files
5. Who can create a spatial map chart?
Any Zoho Analytics user with a spatial data file can create spatial map charts.
Choose the Spatial File option available inside the Files/Feeds tab when your file contains geo-spatial data and the file format matches the list provided above.
6. What is a geometry column in a spatial data table?
A geometry column contains the geodata information which helps in plotting the locations on a map chart. You cannot import a spatial file without the geometry column into Zoho Analytics.
7. Will Zoho Analytics automatically identify the geometry column?
Yes, Zoho Analytics will automatically identify the geometry column in your spatial data file during import.
8. What is a custom-geo column in a spatial data table?
The custom-geo data type are columns in your data that contain unique data and can be used in place of geometry column in the maps you create. Zoho Analytics also identifies custom-geo columns in your data and maps them with the geometry column in the spatial data.
9. Can I import spatial data into an existing table?
Yes, you can import spatial data into an existing table provided the table also contains spatial data.
- You can only Delete existing records and add.
- Other file formats import is not supported into a spatial data table.
Follow the below steps to import spatial data into an existing table:
- Open the table into which you want to import data.
- Click Import Data > Import Data into this Table. The Import wizard to import data into that table will open.
The rest of the steps are same as importing a spatial data file.
10. Are there any restrictions/limitations while importing spatial data files into Zoho Analytics?
In Zoho Analytics, while importing a spatial data file, you must ensure the following:
- You cannot import a spatial file without the geometry column.
- You cannot have multiple geometry columns in a single spatial data file.
- You cannot create a lookup relation with geometry data columns.
- While sharing a spatial data table, you cannot exclude the geometry data column.
- You cannot delete the geometry column in the spatial table.
- You cannot auto analyze a geometry column.
- When you auto-generate reports, the geometry column will not be included in the reports created.
- You cannot create formulas with a geometry column.
- When you export/backup a spatial file, it will not be saved as a spatial data file.
- Zoho Analytics allows you to import a data file having up to 15 MB spatial data.
Creating Geo Charts with Image Background
1. What are geo charts with image background?
In Zoho Analytics, you can blend geo data points (XY coordinates and geo locations) with images to create geo charts with image background. This way you can provide more context to the data being analyzed and gain deeper insights.
Say, you want to analyze a sports team's performance. The team's performance data plotted on the layout of the field/court will provide deeper insights than simply analyzing it as a table or a chart. The below chart illustrates the performance analysis of the basketball team, the Los Angeles Lakers in one of the games.
The below chart is a geo chart with image background that illustrates apparel sales based on brand.
2. What type of data values can be visualized in geo charts with image backgrounds?
You can plot geo data types (both coordinate values and geo locations) over an image.
Coordinate Values (XY) - The coordinate data points are image-specific location points. Say, you want to analyze the floor plan of a construction site. You will have the coordinate values that map to a particular floor plan. Using the geo charts with image background option, you can plot the coordinate values with the corresponding floor plan.
If you do not have the coordinate values of the image being analyzed, you can encode the same from third-party tools like make sense and use the generated values to create geo charts with image backgrounds in Zoho Analytics.
Geo-Location (Lat/Lng) - You can use the geo charts with image background to visualize your geolocation information (say, country, county, city, etc., or latitude and longitude points) over an image.
3. What are the image types supported in geo charts with image background?
Zoho Analytics supports images in .jpeg, .jpg, and .png formats. Ensure that your data tables have the relevant coordinate/geo data points for the images that you are planning to use.
4. How to create geo charts with image background for coordinate values?
The coordinate values are image-specific location points. You can create geo charts with image background if your data tables contain the coordinate values (XY) of the corresponding image that you are planning to use. The below illustration is created with coordinate values corresponding to the human body parts to analyze the apparel sales based on their brands
Let us see how to create the above geo chart with image background.
- From your workspace explorer, click Create > Chart View and select the data table on which you want to create the chart in the Select Base Table dialog. Alternatively, you can also click Create > New Chart from the required data table. You will get navigated to the chart Design Area.
- In the Chart Design Area, drag and drop the X and Y coordinates to the X and Y shelf. Ensure that these values are set to geo data type. You can also change your data type while plotting your charts. To do this, click the Summary Function drop-down in your dropped column and set X - Geo > Longitude and Y - Geo > Latitude.
- Add the other required columns to the corresponding data shelves.
- Navigate to Settings > Maps.
- In the Map Chart Settings page, click the Image option in the Background field.
- In the Image section,
- Click the Choose Image box and add the required image.
- In the Image Scale field, select X and Y scales.
- Mention the Image Scale Values. The image scale values are the plottable image area. It represents the boundary points of the image with respect to the data being plotted. The data values beyond the provided scale values will be ignored. In our case, the X value ranges between 0 to 702 and the Y value ranges between 2122 to 0.
- Lock Aspect Ratio - Select Lock Aspect Ratio if you want to maintain the original ratio of the image. The image aspect ratio will not be retained upon deselecting this option, and it might pixelate the image as the chart size changes.
- Fit to Screen - Select Fit to Screen option if you want to display the images in full-screen mode. You can maintain the aspect ratio of the image when it is enlarged to the screen size by choosing Lock Aspect Ratio along with this option.
- Image Position - Set the image placement location in the draw area using the Image Position drop-down.
- Image Opacity - Set the display opacity (transparency) level for the background image using the Image Opacity scale.
- Data Label - This option allows you to add the Y-axis value as data label on the map chart.
- Fill Opacity - This option allows you to specify the opacity of the chart series color.
- Click Apply.
Geo charts with image background will be successfully created in Zoho Analytics.
5. I have image coordinate values in my data table, but I do not see the Map charts option in Zoho Analytics. Why?
You might have not set the data type of the coordinate values to geo data type. You will be able to see geo map chart option only if your coordinate values is set to geo data type.
Alternatively, you can set the coordinate values to geo data type even while plotting the chart. To do this, click the Summary Function drop-down inline to your dropped column and set X - Geo > Longitude and Y - Geo > Latitude.
Customizing Geo Charts
1. How can I customize the map chart settings?
Zoho Analytics allows you to easily customize the look and feel of your map chart from the settings option.
- Click the Settings option in the toolbar Select the Map tab.
- The Map Chart Settings page will open as shown below. Please do note that the options on this page will differ based on the type of the map chart selected.
- Theme - This option allows you to customize the theme of the map chart.
- Data Label - This option allows you to add Y-axis value as data label on the map chart.
- Fill Opacity (not applicable for Map - Scatter) - This option allows you to specify the opacity of the chart series color.
- Markers Type (applicable only for Map - Scatter) - This option allows you to add a custom marker for the scatter chart.
- Display Specific Country Map - This option allows you to add a map of a particular country alone for the chart.
- Heat Radius (applicable for Geo Heat Map chart) - This option allows you to specify a boundary to combine the data points for heat calculation.
- Heat Intensity (applicable for Geo Heat Map chart) - This option allows you to specify the percentage to intensify the heat of the chart.
- Heat Opacity (applicable for Geo Heat Map chart) - This option allows you to customize the opacity (transparency) of the heat map.
- Once you modified the necessary settings click Apply.
Zoho Analytics offers a wide range of options to customize the chart. Refer here to know more chart setting options that improve the overall appearance of your chart.
2. How do I customize the map chart Theme?
Zoho Analytics provides three themes for the map chart. They are:
- Light - Applies a light grey theme.
- Dark - Applies a dark grey theme.
- Blue - Applies a blue theme.
- Custom - Applies a theme based on custom chosen color.
- Satellite - Applies a satellite map.
Follow the below steps to customize the theme.
- Open the chart you want to customize.
- Click the settings icon. The Settings page will open.
- Open the Maps tab.
- Select the required theme.
- You can choose to invert the land and water color using the Invert Color toggle button. This is applicable for all theme except Satellite map.
- Click Apply. The selected theme will be applied.
3. Can I create the map chart over the satellite map?
Yes, you can create a map chart over the satellite map. Follow the below steps to apply the satellite map theme.
- Open the chart to which you want apply satellite map theme.
- Click the settings icon. The Settings page will open.
- Open the Maps tab.
- Select the Satellite Map as Theme.
- Click Apply. Chart will be plotted over satellite map.
4. Can I use a continuous color range legend for map chart?
Yes, you use a continuous color range legend for map chart and categorize the data values using color range. This will be pretty useful for visualizing data based on the volume of occurrence.
The below animation shows how to do set continuous band as the legend.
5. Can I customize the default home screen of the map chart?
Yes, you can set the default home screen of the map chart.
The below animation shows how to do set default home screen.
6. How do I customize the marker used in the Map - Scatter Chart?
Markers are used to identify the location in a map. Zoho Analytics provides you 6 types of marker types to choose from.
The below animation explains how to change the marker type in a map-scatter chart.
7. How do I customize the color of the charts plotted in the map?
You can customize the chart color of your map charts as you do for other chart types. Please do refer to this documentation to learn more.
8. How do I customize the legend settings in a map chart?
Refer to the legend settings documentation in charts to learn customizing the legend settings in map charts. Please do note that you cannot change the legend position in a map chart.