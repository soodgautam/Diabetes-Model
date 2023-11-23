import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns







def diabetes_proportion_preBalancing (df):
    sns.countplot(x='Diabetes_binary', data=df, palette=("mako"))

    plt.title("Balanced data",size=12, fontstyle='italic', weight=900)
    plt.ylabel("Total Count", size=16, family='monospace')
    plt.xlabel("Diabetes (Non-Diabetes = 0 & Diabetes = 1)", size=16, fontstyle='italic', weight=500)
    plt.savefig("../reports/figures/diabetes_proportion_preBalancing_viz.png")
    plt.show()



def age_and_BMI_histogram (df):
    fig1, ax = plt.subplots(3, 2, figsize=(16,12))

    fig1.suptitle('Age and BMI Histograms')


    fig1.delaxes(ax[2,1])

    fig1.delaxes(ax[2,0])
    fig1.delaxes(ax[1,1])
    fig1.delaxes(ax[1,0])

    ax[0,0].set_title('Age Description')
    sns.histplot(data = df
                ,x = 'Age'
                ,color = 'navy'
                ,alpha = 1
                ,kde = True
                , ax = ax[0,0]
                )
    ax[0,1].set_title('BMI Description')

    sns.histplot(data = df
                ,x = 'BMI'
                ,color = 'indigo'
                ,alpha = 1
                ,kde = True 
                ,ax = ax[0,1]
                )

    fig1.tight_layout()

    plt.savefig("../reports/figures/age_and_BMI_histogram.png")

    plt.show()



def health_description_visual(df):
    fig2, ax = plt.subplots(3, 2, figsize=(16,12))

    fig2.suptitle('Health Histograms')


    fig2.delaxes(ax[2,1]) 

    fig2.delaxes(ax[2,0])
    fig2.delaxes(ax[1,1])



    ax[0,0].set_title('General Health Description')
    sns.histplot(data = df
                ,x = 'GenHlth'
                ,color = 'darkslateblue'
                ,alpha = 1
                ,kde = True 
                ,ax = ax[0,0]
                
                )
    ax[0,1].set_title('Pyshical Health Description')
    sns.histplot(data = df
                ,x = 'PhysHlth'
                ,color = 'navy'
                ,alpha = 1
                ,kde = True 
                ,ax = ax[0,1]
                )
    ax[1,0].set_title('Mental Health Description')
    sns.histplot(data = df
                ,x = 'MentHlth'
                ,color = 'navy'
                ,alpha = 1
                ,kde = True 
                ,ax = ax[1,0]
                , bins = 12
                )

    # set the spacing between subplots
    fig2.tight_layout()

    plt.savefig("../reports/figures/health_descriptions_viz.png")

    plt.show()

    

def general_health_visual (df):
    fig3, ax = plt.subplots(2, 2, figsize=(16,12))

    fig3.suptitle('General Health')

    sns.countplot(x='Sex', data=df, palette=("Blues_d"), ax = ax[0,0])

    ax[0,0].set_xlabel('Sex (0 = Female & 1 = Male)', size=16, fontstyle='italic', weight=500 )
    ax[0,0].set_ylabel('Total Count', size=16, family='monospace')
    ax[0,0].set_title('Sex',size=12, fontstyle='italic', weight=900)

    sns.countplot(x='Smoker', data=df, palette=("Blues_d"),ax = ax[0,1])

    ax[0,1].set_title('Smokers',size=12, fontstyle='italic', weight=900)
    ax[0,1].set_xlabel('Smoker (0 = no & 1 = yes)', size=16, fontstyle='italic', weight=500)
    ax[0,1].set_ylabel('Total Count', size=16, family='monospace')

    sns.countplot(x='HeartDiseaseorAttack', data=df, palette=("Blues_d"),ax = ax[1,0])

    ax[1,0].set_xlabel('Heart Disease (0 = Healthy Heart & 1 = Has Heart Problem)', size=16, fontstyle='italic', weight=500)
    ax[1,0].set_ylabel('Total Count', size=16, family='monospace')
    ax[1,0].set_title('Heart Disease or Attack',size=12, fontstyle='italic', weight=900)

    sns.countplot(x='HeartDiseaseorAttack', data=df, palette=("Blues_d"),ax = ax[1,0])

    ax[1,0].set_xlabel('Heart Disease (0 = Healthy Heart & 1 = Has Heart Problem)', size=16, fontstyle='italic', weight=500)
    ax[1,0].set_ylabel('Total Count', size=16, family='monospace')
    ax[1,0].set_title('Heart Disease or Attack',size=12, fontstyle='italic', weight=900)

    sns.countplot(x='PhysActivity', data=df, palette=("Blues_d"),ax = ax[1,1])

    ax[1,1].set_xlabel('Physical Activity (0 = Non-Physically Acitve & 1 = Physically Active)', size=16, fontstyle='italic', weight=500)
    ax[1,1].set_ylabel('Total Count', size=16, family='monospace')
    ax[1,1].set_title('Physical Activity',size=12, fontstyle='italic', weight=900)


    fig3.tight_layout()

    plt.savefig("../reports/figures/general_health_viz.png")
    plt.show()
    


def healthy_eating(df):
    fig4, ax = plt.subplots(1, 2, figsize=(10,5))

    fig4.suptitle('Healthy eating')

    sns.countplot(x='Fruits', data=df, palette=("Blues_d"), ax = ax[0])

    ax[0].set_xlabel('Eats Fruits (0 = Non-Regulary Acitve & 1 = Regularly)', size=9, fontstyle='italic', weight=500)
    ax[0].set_ylabel('Total Count', size=9, family='monospace')
    ax[0].set_title('Fruit Consumption',size=12, fontstyle='italic', weight=900)

    sns.countplot(x='Veggies', data=df, palette=("Blues_d"), ax= ax[1])

    ax[1].set_xlabel('Eats Vegtables (0 = Non-Regulary Acitve & 1 = Regularly)', size=9, fontstyle='italic', weight=500)
    ax[1].set_ylabel('Total Count', size=9, family='monospace')
    ax[1].set_title('Vegtable Consumption',size=12, fontstyle='italic', weight=900)

    fig4.tight_layout()

    plt.savefig("../reports/figures/eating_habits_viz.png")
    plt.show()
   
    


def health_disorders (df):
    fig5, ax = plt.subplots(3, 2, figsize=(16,12))

    fig5.suptitle('Health Disorders')


    fig5.delaxes(ax[2,1]) 

    fig5.delaxes(ax[2,0])
    fig5.delaxes(ax[1,1])

    sns.countplot(x='HvyAlcoholConsump', data=df, palette=("Blues_d"), ax = ax[0,0])

    ax[0,0].set_xlabel('Alcohol Consumption (0 = Non-Heavy Active & 1 = Heavy)', size=16, fontstyle='italic', weight=500)
    ax[0,0].set_ylabel('Total Count', size=16, family='monospace')
    ax[0,0].set_title('Alcohol Consumption',size=12, fontstyle='italic', weight=900)

    sns.countplot(x='Stroke', data=df, palette=("Blues_d"), ax = ax[0,1])

    ax[0,1].set_xlabel('Stroke (0 = Never Experienced a Stroke & 1 = Has Experienced a Stroke)', size=16, fontstyle='italic', weight=500)
    ax[0,1].set_ylabel('Total Count', size=16, family='monospace')
    ax[0,1].set_title('Stroke',size=12, fontstyle='italic', weight=900)


    sns.countplot(x='HighBP', data=df, palette=("Blues_d"),ax = ax[1,0])



    ax[1,0].set_xlabel('Blood-Pressure(0 = Normal Blood-Pressure & 1 = High Blood-Pressure)', size=16, fontstyle='italic', weight=500)
    ax[1,0].set_ylabel('Total Count', size=16, family='monospace')
    ax[1,0].set_title('Blood-Pressure',size=12, fontstyle='italic', weight=900)
    fig5.tight_layout()

    plt.savefig("../reports/figures/health_disorders_viz.png")

    plt.show()
    

def main ():
    file_path = ("../data/interim/clean_data.csv")
    df = pd.read_csv(file_path)


    print("t1")
    diabetes_proportion_preBalancing (df)


    #viz 2

    age_and_BMI_histogram (df)


    #viz 3

    health_description_visual(df)


    #viz 4

    general_health_visual (df)



    #viz 5
    print("t5")
    healthy_eating(df)


    #viz 6
    print("t6")
    health_disorders (df)





if __name__ == '__main__':
    main()


   
