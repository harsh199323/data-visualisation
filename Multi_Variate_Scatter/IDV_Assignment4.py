import pandas as pd
import plotly as pl
import plotly.express as pex
path='D:/study/Masters/sem-2/IDV/assignments/assignment-4/Assignment 4 - Materials-20200602/DataWeierstrass.csv'

#reading file into 500*500 using dataframe
df = pd.read_csv(path, delimiter=';')

#converting categorical variables(string type) to numeric variables (object type)
#as we cannot use categorical variables to plot
professor_id=[]
lecture_id=[]
for i in range(len(df)):
    professor_id.append(int(df['professor'][i].replace('prof', '')))
    lecture_id.append(int(df['lecture'][i].replace('lecture', '')))
new_professor_data = pd.DataFrame({'professor': professor_id})
new_lecture_data = pd.DataFrame({'lecture': lecture_id})
df.update(new_professor_data)
df.update(new_lecture_data)

#using plotly.express.scatter_matric() for interactive scatter matrix

img=pex.scatter_matrix(df,
    dimensions=['participants','professional expertise','motivation','clear presentation','overall impression'],
                       color="professor",symbol="lecture",
    title="Scatter Matrix",)
img.update_layout(
    title='Scater Matrix',
    dragmode='select',
    width=1000,
    height=1100,
    hovermode='closest',
)
img.update_traces(diagonal_visible=False)
pl.offline.plot(img, filename='scatter_plot.html')
img.show()


#in the below generated plot, hover on sub-matrix to see individual data point characteristics
#and to check for individual professor data characteristics double click on professor or color bar on the right side of matrix, 
#so we can visualize with respect to professor and lecture level

df1=df.copy(deep=True) #creating new copy of original dataframe
#object type to int64
df1['professor']=pd.to_numeric(df1['professor'])
df1['lecture']=pd.to_numeric(df1['lecture'])

#using plotly.express.parallel_coordinates() for interactive scatter matrix
img1=pex.parallel_coordinates(df1,color='overall impression',
                              dimensions=['professor','lecture','participants','professional expertise','motivation','clear presentation','overall impression'],
                               color_continuous_scale=pex.colors.sequential.Inferno,
                               color_continuous_midpoint=2)

pl.offline.plot(img1, filename='parallel_plot.html')
img1.show()
#each row of given data set is represented by polyLine mark, 
#which traverses a set of parallel axes(individual feature attributes)

#drag the lines along the axes to filter over different features
