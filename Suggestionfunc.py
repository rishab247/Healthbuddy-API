import json 
  
def activity_tracker(score=None):
    
    dictionary ={ 
        "Audio Books" : [], 
        "Text Books" : [], 
        "Meditation Techniques" : [], 
        "ACtivities" : []
    }  
    
    if score == "happiness":
        dictionary ={ 
            "Audio Books" : ["You Are a Badass"," How To Win Friends & Influence People","The Power of Now"], 
            "Text Books" : ["You Are a Badass at Making Money","The Power of Positive Leadership"], 
            "Meditation Techniques" : ["Loving-kindness meditation","Mindfulness meditation"], 
            "ACtivities" : ["Acting","Flying a plane","Buying gifts","Bike riding","Make lists of tasks","Listening to music","Photography"]
        } 
    elif score == "sadness":
        dictionary ={ 
            "Audio Books" : [" Sacred Hoops","How To Win Friends & Influence People","The Life-Changing Magic of Tidying Up"], 
            "Text Books" : ["Win Bigly","The 5 Second Rule","Captivate"], 
            "Meditation Techniques" : ["Zen meditation","Mindfulness meditation","Kundalini yoga"], 
            "ACtivities" : ["Going to a movie","Jogging or walking","Listening to music","Meeting new people"]
        }  
    elif score == "neutral" or score == None:
        dictionary ={ 
            "Audio Books" : ["How To Win Friends & Influence People","Get a Financial Life","The 4-Hour Workweek"], 
            "Text Books" : ["You Are a Badass at Making Money","The Power of Positive Leadership","Win Bigly","Unshakeable","The Art of War"], 
            "Meditation Techniques" : ["Kundalini yoga","Zen meditation","Mindfulness meditation","Loving-kindness meditation"], 
            "ACtivities" : ["Playing cards","Playing computer games","Doing something new","Listening to music"]
        }  
    elif score == "anger":
        dictionary ={ 
            "Audio Books" : ["The Art of War","How to Win Friends & Influence People","7 Habits of Highly Effective People","The Magic of Thinking Big"," The Four Agreements"], 
            "Text Books" : ["The 5 Second Rule","You Are a Badass at Making Money","The Power of Positive Leadership"], 
            "Meditation Techniques" : ["Alome Vilome","Usprasana","Sukhasana","Parivrtta Anjaneyasana","Utkata konasana","Savasana"], 
            "ACtivities" : ["Meeting new people","Remembering beautiful scenery","Listening to music","Going for a holiday"]
        }  
    elif score == "disgust":
        dictionary ={ 
            "Audio Books" : ["How to Win Friends & Influence People","The Magic of Thinking Big","Don’t Sweat the Small Stuff and Its All Small Stuff"], 
            "Text Books" : ["Sacred Hoops","Unshakeable","Win Bigly","The Power of Positive Leadership"], 
            "Meditation Techniques" : ["Kundalini yoga","Zen meditation","Savasana","Parivrtta Anjaneyasana","Alome Vilome"], 
            "ACtivities" : ["Reading","Playing volleyball","Dressing up and looking nice"]
        }      

    return dictionary
    


