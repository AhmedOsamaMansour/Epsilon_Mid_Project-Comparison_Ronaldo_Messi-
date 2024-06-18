# imports
import pandas as pd
import streamlit as st
import seaborn as sns
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import plotly.figure_factory as ff

# reading Dataset
df = pd.read_csv('updated_messi_ronaldo_dataset.csv')
st.sidebar.title('Messi - Ronaldo Project')
st.sidebar.info("This project is about comparing the football legends Lionel Messi and Cristiano Ronaldo using different visualizations.")

# Path to your background image
background_image_path = "images/4.jpg"

# Read the image and convert it to a base64 string
import base64

def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

def set_background_image(image_path):
    bin_str = get_base64_of_bin_file(image_path)
    css = f"""
    <style>
    .stApp {{
        background-image: url("data:image/jpeg;base64,{bin_str}");
        background-size: cover;
    }}
    </style>
    """
    st.markdown(css, unsafe_allow_html=True)

# Set the background image
set_background_image(background_image_path)

def into_Data():
    st.markdown(
        """
        <style>
        .font20px {
            font-size: 26px !important;
            text-align: center !important;
        }
        table {
            margin: auto;
        }
        th, td {
            text-align: center !important;
            font-weight:bold !important;
            height: 50px !important;
        }
        </style>
        """, 
        unsafe_allow_html=True
    )

    result = st.sidebar.radio('Select the option you want', ['player information', 'Champion', 'individual awards'])
    
    if result == 'player information':
        table1 = pd.read_csv('table1.csv', encoding='cp1256')
        st.markdown('<div class="font20px">', unsafe_allow_html=True)
        st.table(data=table1)
        st.markdown('</div>', unsafe_allow_html=True)
    elif result == 'Champion':
        table2 = pd.read_csv('table2.csv', encoding='cp1256')
        st.markdown('<div class="font20px">', unsafe_allow_html=True)
        st.table(data=table2)
        st.markdown('</div>', unsafe_allow_html=True)
    else:
        table3 = pd.read_csv('table3.csv', encoding='cp1256')
        st.markdown('<div class="font20px">', unsafe_allow_html=True)
        st.table(data=table3)
        st.markdown('</div>', unsafe_allow_html=True)
def ronaldoPage():
    st.markdown("<h1 style = 'text-align : center ; color : white;'>{}</h1>".format(select_page), unsafe_allow_html=True )
    ronaldoData = df[df['player_name']=='ronaldo']
    col1,col2 = st.columns(2)
    with col1:
        st.plotly_chart(px.histogram(data_frame=ronaldoData,x='club',color='club',height=450,width = 800,text_auto=True,title='number of goal for each club:',
                                     color_discrete_map={'Real Madrid':'#150ee6','Juventus FC':'#ffffff',
                                                         'Manchester United':'#C70039', 'Al-Nassr FC':'#F8DE22',
                                                         'Sporting CP': 'green'}))
    with col2:
        st.plotly_chart(px.pie(data_frame=ronaldoData,names='club',color='club',height=450,width = 500,title='percentage of number of goal for each club:',
                               color_discrete_map={'Real Madrid':'#150ee6','Juventus FC':'#ffffff', 
                                                   'Manchester United':'#C70039', 'Al-Nassr FC':'#F8DE22',
                                                   'Sporting CP': 'green'}))
    st.plotly_chart(px.histogram(data_frame=ronaldoData,x='season',text_auto=True,title='number of goals per season:',color='club',color_discrete_map={'Real Madrid':'#150ee6',
                'Juventus FC':'#ffffff', 'Manchester United':'#C70039', 'Al-Nassr FC':'#F8DE22','Sporting CP': 'green'}))
    
    st.plotly_chart(px.histogram(data_frame=ronaldoData,x='type',text_auto=True,title='number of goal for each type:',
        color='type',color_discrete_map={'Solo run':'#150ee6','Header':'#ffffff',
        'Right-footed shot':'#C70039', 'Left-footed shot':'#F8DE22',
            'Direct free kick': 'green','Tap-in':'yellow','Penalty':'gray', 'Penalty rebound':'#cc34eb',
               'Long distance kick':'#05ffc9', 'Counter attack goal':'#7aff05',
               'Deflected shot on goal':'#f707e3', 'Chest':'#79cffc'}).update_xaxes(categoryorder='total descending').update_layout(yaxis_title="number of goals"))
    
    st.plotly_chart(px.pie(data_frame=ronaldoData,names='type',title='percentage of number of goal for each type:',
            color_discrete_sequence=['#150ee6','#ffffff','#C70039','#F8DE22','green','yellow','gray','#cc34eb','#05ffc9','#7aff05',
               '#f707e3','#79cffc']))
    
    st.plotly_chart(px.histogram(data_frame=ronaldoData,x='venue',color='club',barmode='group',text_auto=True,title='number of goal for each venue (home or away):',
                                     color_discrete_map={'Real Madrid':'#150ee6','Juventus FC':'#ffffff',
                                                         'Manchester United':'#C70039', 'Al-Nassr FC':'#F8DE22',
                                                         'Sporting CP': 'green'}))
    
    st.plotly_chart(px.histogram(data_frame=ronaldoData,x='playing_position',text_auto=True,color='playing_position',title="total goals in different position:",color_discrete_map={'CF':'#150ee6','RW':'#F8DE22','LW':'#C70039','SS':'green'}).update_xaxes(categoryorder='total ascending'))
    
    st.plotly_chart(px.histogram(data_frame=ronaldoData,x='playing_position',color='club',text_auto=True,title="total goals in different position:",color_discrete_map={'Real Madrid':'#950dfc','Juventus FC':'#ffffff',
                                                         'Manchester United':'#C70039', 'Al-Nassr FC':'#F8DE22',
                                                         'Sporting CP': 'green'}))
    
    
    unique_matches = ronaldoData.drop_duplicates(subset='date').reset_index()
    unique_matches['win_loss'] = unique_matches['club_score'] - unique_matches['opponent_score']
    def win_or_loss(value):
        if value >0:
            return 'win'
        elif value ==0:
            return 'draw'
        else:
            return 'loss'
    unique_matches['win_loss'] = unique_matches['win_loss'].apply(win_or_loss)
    st.plotly_chart(px.pie(data_frame=unique_matches,names='win_loss',hole=0.6,title='The percentage of wins, losses and draws in matches in which Ronaldo scored goals:',color_discrete_sequence=['#C70039','#ffffff','#F8DE22']))
    
    def update_goal_time(x):
        if '45+' in x:
            x = '45'
        if eval(x) <= 45:
            return 'first half'
        elif '90+'in x:
            return 'plus 90'
        elif '+' not in x and eval(x) <=90:
            return 'second time'
        else:
            return 'extra time'
    ronaldoData['match_periods'] = ronaldoData['minute'].apply(update_goal_time)
    st.plotly_chart(px.histogram(data_frame=ronaldoData,x='match_periods',text_auto=True,title='Goal Period:',color='match_periods',color_discrete_map={'first half':'#150ee6','plus 90':'#ffffff','second time':'#C70039','extra time':'#F8DE22'}).update_xaxes(categoryorder='total descending'))
    
    top_5_victims_club = ronaldoData.groupby('opponent')['player_name'].count().sort_values(ascending = False).head(5).reset_index()
    st.plotly_chart(px.histogram(data_frame=top_5_victims_club , x ='player_name' ,y='opponent',text_auto=True,color='opponent',color_discrete_map={'Sevilla FC':'gold','Atletico de Madrid':'#C70039','Getafe CF':'green','Celta de Vigo':'#79a3fc','FC Barcelona':'darkblue'}).update_yaxes(categoryorder='total ascending'))
    
    hattricks_3_goals = ronaldoData[ronaldoData.groupby('date')['player_name'].transform('count')>2]
    st.plotly_chart(px.histogram(data_frame=hattricks_3_goals,x='competition',text_auto=True,title='count of Ronaldo Hattricks in different competition:',color='competition',color_discrete_map={
        'Premier League':'#150ee6','LaLiga':'#ffffff','Saudi Pro League	':'#C70039','UEFA Champions League':'#F8DE22','Copa del Rey':'green',
        'Serie A':'#7aff05','FIFA Club World Cup':'#f707e3'
    }).update_xaxes(categoryorder='total descending'))
    
    top_5_assist = ronaldoData.groupby('goal_assist')['player_name'].count().sort_values(ascending = False).head(5).reset_index()
    st.plotly_chart(px.histogram(data_frame=top_5_assist,x='goal_assist',y='player_name',text_auto=True,title='Top 5 Player Make Assist To Ronaldo:',
        color='goal_assist',color_discrete_map={
        'Karim Benzema':'#150ee6','Gareth Bale':'#ffffff','Mesut Ozil':'#C70039','Marcelo':'#F8DE22','Ryan Giggs':'green'
    }))
    
    st.plotly_chart(px.histogram(data_frame=ronaldoData[ronaldoData['competition']=='UEFA Champions League'],text_auto=True,x ='matchday',title="total goals in champions league stages:",color='matchday',color_discrete_map={
        'group stage':'#150ee6','quarter-finals':'#ffffff','last 16':'#C70039','semi-finals':'#F8DE22','final':'green'
    }).update_xaxes(categoryorder='total descending'))
    st.plotly_chart(px.histogram(data_frame=ronaldoData[ronaldoData['competition']=='Premier League'],text_auto=True,x =ronaldoData['month_name'].astype(str),title='number of goals for each month:',color_discrete_sequence=['gold']).update_xaxes(categoryorder='total descending').update_layout(yaxis_title="number of goals"))
    
def messiPage():
    messiData = df[df['player_name']== 'messi']
    st.markdown("<h1 style = 'text-align : center ; color : blue;'>{}</h1>".format(select_page), unsafe_allow_html=True )
    #st.write('Tarek')
    col1,col2 = st.columns(2)
    with col1:
        st.plotly_chart(px.histogram(data_frame=messiData,x='club',color='club',height=450,width = 800,text_auto=True,title='number of goal for each type:',
                                     color_discrete_map={'Paris Saint-Germain':'#150ee6','FC Barcelona':'#C70039'}))
    with col2:
        st.plotly_chart(px.pie(data_frame=messiData,names='club',color='club',height=450,width = 500,title='percentage of number of goal for each type:',
                               color_discrete_map={'Paris Saint-Germain':'#150ee6','FC Barcelona':'#C70039'}))
    st.plotly_chart(px.histogram(data_frame=messiData,x='season',text_auto=True,title='number of goals per season:',color='club',
                                 color_discrete_map={'Paris Saint-Germain':'#150ee6','FC Barcelona':'#C70039'}))
    
    st.plotly_chart(px.histogram(data_frame=messiData,x='type',text_auto=True,title='number of goal for each type:',
        color='type',color_discrete_map={'Solo run':'#150ee6','Header':'#ffffff',
        'Right-footed shot':'#C70039', 'Left-footed shot':'#F8DE22',
            'Direct free kick': 'green','Tap-in':'yellow','Penalty':'gray', 'Penalty rebound':'#cc34eb',
               'Long distance kick':'#05ffc9', 'Counter attack goal':'#7aff05',
               'Deflected shot on goal':'#f707e3', 'Chest':'#79cffc'}))
    
    st.plotly_chart(px.pie(data_frame=messiData,names='type',title='percentage of number of goal for each type:',
            color_discrete_sequence=['#150ee6','#ffffff','#C70039','#F8DE22','green','yellow','gray','#cc34eb','#05ffc9','#7aff05',
               '#f707e3','#79cffc']))
    
    st.plotly_chart(px.histogram(data_frame=messiData,x='venue',color='club',barmode='group',text_auto=True,title='number of goal for each venue (home or away):',
                                     color_discrete_map={'Paris Saint-Germain':'#150ee6','FC Barcelona':'#C70039'}))
    st.plotly_chart(px.histogram(data_frame=messiData,x='playing_position',color='playing_position',text_auto=True,title="total goals in different position:",color_discrete_map={'CF':'#150ee6','RW':'#F8DE22','LW':'#C70039','SS':'green','AM':'yellow'}).update_xaxes(categoryorder='total ascending'))
    
    st.plotly_chart(px.histogram(data_frame=messiData,x='playing_position',color='club',title="total goals in different position for each club:",text_auto=True,color_discrete_map={'Paris Saint-Germain':'#150ee6','FC Barcelona':'#C70039'}).update_xaxes(categoryorder='total ascending').update_layout(yaxis_title="number of goals"))
    
    unique_matches = messiData.drop_duplicates(subset='date').reset_index()
    unique_matches['win_loss'] = unique_matches['club_score'] - unique_matches['opponent_score']
    def win_or_loss(value):
        if value >0:
            return 'win'
        elif value ==0:
            return 'draw'
        else:
            return 'loss'
    unique_matches['win_loss'] = unique_matches['win_loss'].apply(win_or_loss)
    st.plotly_chart(px.pie(data_frame=unique_matches,names='win_loss',hole=0.6,title='The percentage of wins, losses and draws in matches in which Messi scored goals:',color_discrete_sequence=['#C70039','#ffffff','#F8DE22']))
    
    def update_goal_time(x):
        if '45+' in x:
            x = '45'
        if eval(x) <= 45:
            return 'first half'
        elif '90+'in x:
            return 'plus 90'
        elif '+' not in x and eval(x) <=90:
            return 'second time'
        else:
            return 'extra time'
    messiData['match_periods'] = messiData['minute'].apply(update_goal_time)
    st.plotly_chart(px.histogram(data_frame=messiData,x='match_periods',text_auto=True,title='Goal Period:',color='match_periods',color_discrete_map={'first half':'#150ee6','plus 90':'#ffffff','second time':'#C70039','extra time':'#F8DE22'}).update_xaxes(categoryorder='total descending'))
    
    top_5_victims_club = messiData.groupby('opponent')['player_name'].count().sort_values(ascending = False).head(5).reset_index()
    st.plotly_chart(px.histogram(data_frame=top_5_victims_club , title = 'Top five most victimized clubs of Messi:' ,x ='player_name' ,y='opponent',text_auto=True,color_discrete_sequence=['#C70039']).update_yaxes(categoryorder='total ascending'))
    
    hattricks_3_goals = messiData[messiData.groupby('date')['player_name'].transform('count')>2]
    st.plotly_chart(px.histogram(data_frame=hattricks_3_goals,x='competition',text_auto=True,title='count of Messi Hattricks in different competition:',color='competition',color_discrete_map={
        'Premier League':'#150ee6','LaLiga':'#ffffff','Supercopa':'#C70039','UEFA Champions League':'#F8DE22','Copa del Rey':'green',
        'Ligue 1':'#7aff05'
    }).update_xaxes(categoryorder='total descending'))
    
    top_5_assist = messiData.groupby('goal_assist')['player_name'].count().sort_values(ascending = False).head(5).reset_index()
    st.plotly_chart(px.histogram(data_frame=top_5_assist,x='goal_assist',y='player_name',text_auto=True,title='Top 5 Player Make Assist To Ronaldo:',
        color='goal_assist',color_discrete_map={
        'Luis Suarez':'#150ee6','Dani Alves':'#ffffff','Andres Iniesta':'#C70039','Xavi':'#F8DE22','Neymar':'green'
    }))
    
    st.plotly_chart(px.histogram(data_frame=messiData[messiData['competition']=='UEFA Champions League'],x ='matchday',title="total goals in champions league stages:",color='matchday',color_discrete_map={
        'group stage':'#150ee6','quarter-finals':'#ffffff','last 16':'#C70039','semi-finals':'#F8DE22','final':'green'
    },text_auto=True).update_xaxes(categoryorder='total descending'))
    st.plotly_chart(px.histogram(data_frame=messiData[messiData['competition']=='Premier League'],x =messiData['month_name'].astype(str),text_auto=True,
    title='number of goals for each month:',color_discrete_sequence=['darkblue']).update_xaxes(
    categoryorder='total descending').update_layout(xaxis_title="month name", yaxis_title="number of goals"))

    
def compare_allClubs():
    st.plotly_chart(px.pie(data_frame=df,names='player_name',title='number of playing matches with their teams:',color_discrete_sequence=['#ffffff','darkblue']))
    
    st.plotly_chart(px.histogram(data_frame=df,y='season',color='player_name',title='number of goals for each season:',height=1500,text_auto=True,barmode='group',color_discrete_sequence=['white','darkblue']).update_xaxes(categoryorder='total ascending').update_layout(xaxis_title="number of goals"))
    st.plotly_chart(px.histogram(data_frame=df,x='type',color='player_name',title='How to Score The Goal:',text_auto=True,barmode='group',color_discrete_sequence=['#ffffff','darkblue']).update_xaxes(categoryorder='total ascending'))
     
    st.plotly_chart(px.histogram(data_frame= df,x = 'season_time',title='number of goals per season periods:',color='player_name',color_discrete_sequence=['#ffffff','darkblue'],barmode='group',text_auto=True))
    
    st.plotly_chart(px.histogram(data_frame=df,x=df['player_goal_number'].astype(str),text_auto=True,title='sum of goal number:',color='player_name',color_discrete_sequence=['#ffffff','darkblue'],barmode='group'))
    
    st.plotly_chart(px.histogram(data_frame=df[df['competition']=='UEFA Champions League'],x ='matchday',title='UEFA Champions League',color='player_name',barmode='group',color_discrete_sequence=['#ffffff','darkblue']).update_xaxes(categoryorder='total descending'))

    unique_matches = df.drop_duplicates(subset='date').reset_index()
    unique_matches['win_loss'] = unique_matches['club_score'] - unique_matches['opponent_score']
    def win_or_loss(value):
        if value > 0:
            return 'win'
        elif value == 0:
            return 'draw'
        else:
            return 'loss'
    unique_matches['win_loss'] = unique_matches['win_loss'].apply(win_or_loss)
    st.plotly_chart(px.pie(data_frame=unique_matches,names='win_loss',hole=0.6,title='percentages of lose, win and draw when player score goal in match:',
                           facet_col='player_name',color_discrete_sequence=['darkblue','#ffffff','red']))
    
    

def compare_Real_barca():
    realMadrid_Barcelona  = df[(df['date'] >= '2009/08/29') & (df['date'] <= '2018-05-19')]

    st.plotly_chart(px.histogram(data_frame=realMadrid_Barcelona,y='season',color='player_name',title='number of goals for each season:',height=1500,text_auto=True,barmode='group',color_discrete_sequence=['white','darkblue']).update_xaxes(categoryorder='total ascending').update_layout(xaxis_title="number of goals"))

    st.plotly_chart(px.histogram(data_frame=realMadrid_Barcelona,x='player_name',color='player_name',title='When Ronaldo is in Real Madrid and Messi is in Barcelona:',text_auto=True,color_discrete_map={'messi':'darkblue','ronaldo':'white'}).update_layout(yaxis_title="number of goals"))
    
    st.plotly_chart(px.pie(data_frame=realMadrid_Barcelona,names='player_name',title= 'percentage of goals when ronaldo is in real madrid and messi is in barcelona:',color_discrete_sequence=['darkblue','#ffffff']))
    
    unique_matches = realMadrid_Barcelona.drop_duplicates(subset='date').reset_index()
    unique_matches['win_loss'] = unique_matches['club_score'] - unique_matches['opponent_score']
    def win_or_loss(value):
        if value > 0:
            return 'win'
        elif value == 0:
            return 'draw'
        else:
            return 'loss'
    unique_matches['win_loss'] = unique_matches['win_loss'].apply(win_or_loss)
    st.plotly_chart(px.pie(data_frame=unique_matches,names='win_loss',hole=0.6,title='percentages of lose, win and draw when player score goal in match (ronaldo in real madrid and messi in barcelona):',
                           facet_col='player_name',color_discrete_sequence=['darkblue','white','red']))
    
    msk1= realMadrid_Barcelona['competition']=='UEFA Champions League'
    msk2= realMadrid_Barcelona['competition']=='LaLiga'
    champions_league_data = realMadrid_Barcelona[msk1 | msk2]
    st.plotly_chart(px.histogram(data_frame=champions_league_data,x ='competition',title = 'number of goals per competition:',color='player_name',barmode='group',text_auto=True,color_discrete_map={'ronaldo':'white','messi':'darkblue'}).update_layout(yaxis_title="number of goals"))
    
    st.plotly_chart(px.histogram(data_frame=realMadrid_Barcelona[realMadrid_Barcelona['competition']=='UEFA Champions League'],x ='matchday',text_auto=True,title='UEFA Champions League:',color='player_name',barmode='group',color_discrete_sequence=['white','darkblue']).update_xaxes(categoryorder='total descending').update_layout(yaxis_title="number of goals"))
    
    
def comparePage():
    save_radio = st.sidebar.radio('select option do you want about ronaldo and messi:',['all clubs','real madrid - barcelona'])
    
    st.markdown("<h1 style = 'text-align : center ; color : blue;'>Welcome To Comparison of Messi and Ronaldo in Europe</h1>", unsafe_allow_html=True )
    st.image('images/messi_ronaldo.png')
    if save_radio == 'all clubs':
        compare_allClubs()
    elif save_radio == 'real madrid - barcelona':
        compare_Real_barca()
    
    
# pages:
pages = {
    'intoduction': into_Data,
    'Ronaldo': ronaldoPage,
    'Messi': messiPage,
    'Comparison': comparePage
}
select_page = st.sidebar.selectbox('Select Page That You Want:',pages.keys())
pages[select_page]()
