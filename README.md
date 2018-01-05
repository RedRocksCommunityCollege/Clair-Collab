# Clair-Collab

### An exploratory collaborative in data science, analytics, and visualization between Red Rocks Community College's DataLab and Clair.

|Section|Content|
|:---:|:---:|
|1|The Report|
|2|The Results|
|3|The Repository|
___
#### 1. THE REPORT  

**Objectives**
The primary intention of this collaboration was to foster experiential learning using real-world (anonymized) data provided by Clair. In return, as the student, I had a secondary intention of returning some finished product, that I hoped would be of interest or use to Clair.

**Outcome**
The primary objective of experienced-based learning was met unquestionably. I started this project with virtually no coding, large data set, or computer science experience of any kind and I am leaving it with a basic working knowledge of:

* The Python coding language and the following modules:
  * Pandas for data cleaning and manipulation
  * Numpy for mathematical operations on numerical data
  * Re for mining text data
  * URLlib for web scraping
  * Plot.ly and MatPlotLib for data visualization
* Git and Github for version control and collaboration
* Dealing with large data sets

Equally as important as these specific skills, this project has allowed me to become more comfortable with using computers in general. I have gone from being intimidated by command line, to independently learning programs designed for developers.

The second objective, of returning something of interest or value back to Clair, proved to be a bit more challenging. Some of the struggles included:
* Learning to code
* Getting machine learning programs such as Tensorflow, SciKitLearn, and others to run and learning how to use them.  

I need to learn more about neural networks and then revisit this problem in the future.

In addition to the finished products, (which I'll demonstrate in the next section,) there are a few unfinished pieces I would like to revisit in the future. Mainly, analyzing bandwidth's relationship to time, event size, and other variables using machine learning powered linear regression. Ultimately, I'd like to use those findings to create a utility for projecting bandwidth requirements for future event.
___
#### 2. THE RESULTS

After isolating a single event from the "secure_devices.csv" data set, we began exploring a few of the metrics. One of the most interesting columns was "srccountry." We learned that there were 52 unique source countries in the single event we isolated. They were distributed across the globe in a manor that suggested that "srccountry" somehow represents the country of origin of an attendee.

It seemed that this information could be interesting in a visualization; So we created two choropleths (a map with shaded regions depicting a statistical variable.)

The first, based on our assumptions, depicts the geographic demography of event attendees.
<div>
    <a href="https://plot.ly/~CoryK8nn8dy/17/?share_key=WrKdwWlCG5GcTduZE7Z5Sl" target="_blank" title="Plot 17" style="display: block; text-align: center;"><img src="https://plot.ly/~CoryK8nn8dy/17.png?share_key=WrKdwWlCG5GcTduZE7Z5Sl" alt="Plot 17" style="max-width: 100%;width: 600px;"  width="600" onerror="this.onerror=null;this.src='https://plot.ly/404.png';" /></a>
    <script data-plotly="CoryK8nn8dy:17" sharekey-plotly="WrKdwWlCG5GcTduZE7Z5Sl" src="https://plot.ly/embed.js" async></script>
</div>

<br>
The second describes relative bandwidth usage by country based on transaction quantity and size.
<div>
    <a href="https://plot.ly/~CoryK8nn8dy/15/?share_key=g78H8pL7dm9OzR1a4BEqVP" target="_blank" title="Plot 15" style="display: block; text-align: center;"><img src="https://plot.ly/~CoryK8nn8dy/15.png?share_key=g78H8pL7dm9OzR1a4BEqVP" alt="Plot 15" style="max-width: 100%;width: 600px;"  width="600" onerror="this.onerror=null;this.src='https://plot.ly/404.png';" /></a>
    <script data-plotly="CoryK8nn8dy:15" sharekey-plotly="g78H8pL7dm9OzR1a4BEqVP" src="https://plot.ly/embed.js" async></script>
</div>
<br>
The code that generates these visualizations was written to be a reusable utility. A user should be able to import any Fortigate router data of a similar format, isolate the lines they are interested in, and run the code to see visualizations of their event.

___
#### 1. THE REPOSITORY

_**All of the material in this repository is available for unrestricted use by Clair and any other party that wishes to use it constructively.**_  

|Section|Content|
|:---:|---|
|Data|Data provided by Clair, output from code, and artificial data created for testing and learning|
|Tools|Scripts that may be useful within other code for this project|
|Future Development|Code to serve as a starting point upon revisiting the machine learning/ linear regression/ bandwidth prediction portion of this project|
|Final Products|Code that produces the Choropleths in the previous section|

**Acknowledgements** I would like to express my gratitude to Clair for providing this priceless learning opportunity, and to Adam Forland, my math professor and research advisor, for guiding and inspiring me throughout the entire project.

<br>

**For more information**  
Please contact project lead:  
Cory Kennedy  
GitHub User: CoryK8nn8dy  
Email: K8NN8DY@gmail.com
