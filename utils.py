
import numpy as np
import matplotlib.pyplot as plt

def annotate(ax, title='', strformat='', divideby=1):
    # Annotate
    for p in ax.patches:
        # format(, '.1f')
        value = p.get_height()/divideby
        ax.annotate(f"{value:.1f}{strformat}", 
                    (p.get_x() + p.get_width() / 2., p.get_height()), 
                    ha = 'center', va = 'center', 
                    xytext = (0, 9), 
                    textcoords = 'offset points')
    ax.set_title(title)

from mpl_toolkits.axes_grid1 import make_axes_locatable
def addColorbar():
    fig, ax = plt.subplots(1, 1, figsize=(20, 16))
    divider = make_axes_locatable(ax)
    cax = divider.append_axes("right", size="2%", pad="0.5%")
    return ax, cax


def colDetails(cols, label):
    print(f"\n{label}: {len(cols)} {cols}")

def colInfo(df, columns):
    for col in columns:
        if df[col].dtype == object:
            if df[col].isnull().sum() > 0:
                values = df[col].unique().tolist()
            else:
                values = sorted(df[col].unique().tolist())
            print(f"{col}: {len(values)} : {values}")
        else:
            #print(f"{col}: {df[col].describe()}")
            # TODO: mean, min, 25, 50, 75, max
            print(f"{col}: {df[col].mean():.0f} {df[col].quantile([0, .25, .50, .75, 1 ]).values.tolist()} ")

    df[columns][:5]


'''
showValues: If number of values are high, then pass False

OUTPUT:

'''
def colInfo1(df, col, showValues=True):
    total = df.shape[0]
    null = df[df[col].isnull()][col].shape[0]

    print(f"{col:10}: {df[col].dtype.name:7} : {null:4}, {100*null/total:0.1f}% : ", end='')

    if showValues == True:
        if df[col].dtype == object:
            unique = df[col].unique().tolist()
            unique = list(set(unique) - {np.nan})
            unique = sorted(unique)
            if df[col].isnull().sum() > 0:
                unique = ['nan'] + unique
            print(f"{len(unique):4}, {100*len(unique)/total:0.1f}% : {unique}", end='')
        else:
            #print(f"{col}: {df[col].describe()}")
            # TODO: mean, min, 25, 50, 75, max
            print(f"{df[col].mean():.0f} {df[col].quantile([0, .25, .50, .75, 1 ]).values.tolist()} ", end='')
    
    print()

def showColumns(df, columns):
    for col in columns:
        colInfo1(df, col)


def getNullColumns(df):
    print(df[df.columns[df.isnull().any()]].isnull().sum())

def checkUnique(df, col):
    total = df.shape[0]
    unique = df[col].unique().shape[0]
    print(f"{col}: {unique}, {100*unique/total}%")
