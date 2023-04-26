def Datenvorbereitung(df):
    """
    
    """
    ### DAS NOCH IN EINE FUNKTION PACKEN ###
    MaStRWind = df[df['Inbetriebnahmedatum'].notna()]
    MaStRWind.loc[:,"Inbetriebnahmejahr"] = MaStRWind['Inbetriebnahmedatum'].dt.year
    MaStRWind.loc[:,"Inbetriebnahmemonat"] = MaStRWind['Inbetriebnahmedatum'].dt.month
    MaStRWind.loc[:,"Inbetriebnahmewochentag"] = MaStRWind['Inbetriebnahmedatum'].dt.day_of_week

    MaStRWind.loc[:,"Bundesland"] = MaStRWind["Bundesland"].cat.rename_categories({"1416":"Offshore"})
    #MaStRWind["Inbetriebnahmewochentag"] = MaStRWind["Inbetriebnahmewochentag"].replace({0:"Montag",1:"Dienstag",2:"Mittwoch",3:"Donnerstag",4:"Freitag",5:"Samstag",6:"Sonntag"})
    return MaStRWind