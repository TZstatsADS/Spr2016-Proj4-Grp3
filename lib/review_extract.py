import csv

def trycast(x):
    try:
        return float(x)
    except:
        try:
            return int(x)
        except:
            return x


def count_cat(category,review):
    n = 0
    for word in category:
        n = n + review.count(word)
    return(n)

cols = ['product_productid', 'review_userid', 
        'review_helpfulness', 'review_score',
        'action_adv_war_n','sports_n','family_ani_n','comedy_n',
        'mystery_drama_n','doc_bio_hist_n','musical_n','horror_n',
        'romance_n','western_n']

# Category key words collection
action_adv_war = ['action','adventure','war','risk','explosi','fight','daring',
                  'escape','hero','blood','brother','duty','honor','violence',
                  'militar','warrior','spy','mission','gun','gadget']
sports = ['sport','team','football','baseball','hockey','soccer','coach',
          'college','game','athlete','ESPN','quarterback','cheerlead',
          'basketball','skating','NFL','NBA','rival','score','goal']
family_ani = ['anima','family','general','cartoon','paint','young','illusion',
              'age','figurine','computer­generated','magic','audience','figure',
              'puppet','pixel','creative','appropriate','fairy','child','home']
comedy = ['comedy','funny','comic','laugh','satir','humor','sketch','fancy',
          'excite','entertain','parody','mock','lighthearted','pun','amuse',
          'stand­up','satire','screwball','joke','improvise']
mystery_drama = ['noir','crime','drama','mystery','serious','cynic','heavy',
                 'detect','evil','puzzle','police','investigate','dark','melo',
                 'erotic','cruel','goth','gang','legal','suspense']
doc_bio_hist = ['document','biograph','histori','real­world','journal','true',
                'narrative','literary','docudrama','education','nonfiction',
                'reality','fact','opinion','fact','century','politic',
                'personal','expert','memoir']
musical = ['music','danc','production','stage','broadway','theater','song',
           'show','choreo','sing','orchestra','sound','vocal','costume',
           'number','rock','disco','classical','cappella','instrument']
horror = ['thrill','science','fantasy','horror','extraterrestrial','alien',
          'space','robot','twist','psycho','fascinat','whodunit','mind','trap',
          'kill','monster','scary','torture','terror','demon']
romance = ['romance','love','heart','triangle','passion','emotion','sex',
           'relation','affection','date','marri','sentiment','friends','chick',
           'cute','feel','match','interest','beaut','like']
western = ['west','american','old','cowboy','revolve','rifle','horse','boot',
           'native','bounty','hunter','outlaw','settler','town','spur',
           'cavalry','ranch','sling','saloon','wild']

f = open('./moviescsv.csv', 'w')
w = csv.writer(f)
w.writerow(cols)

doc = {}
i = 1
with open('./movies.txt', encoding="utf-8", errors="surrogateescape") as infile:
    for line in infile:
        line = line.strip()
        if line == "" and 'review_text' in doc:
            
            i = i+1
            review=doc['review_summary'].lower()+' '+doc['review_text'].lower()
            action_adv_war_n = count_cat(action_adv_war,review)
            sports_n = count_cat(sports,review)
            family_ani_n = count_cat(family_ani,review)
            comedy_n = count_cat(comedy,review)
            mystery_drama_n = count_cat(mystery_drama,review)
            doc_bio_hist_n = count_cat(doc_bio_hist,review)
            musical_n = count_cat(musical,review)
            horror_n = count_cat(horror,review)
            romance_n = count_cat(romance,review)
            western_n = count_cat(western,review)

            total = (action_adv_war_n+sports_n+family_ani_n+comedy_n
                +mystery_drama_n+doc_bio_hist_n+musical_n+horror_n
                +romance_n+western_n)
            if total == 0:
                doc['action_adv_war_n'] = 0
                doc['sports_n'] = 0
                doc['family_ani_n'] = 0
                doc['comedy_n'] = 0
                doc['mystery_drama_n'] = 0
                doc['doc_bio_hist_n'] = 0
                doc['musical_n'] = 0
                doc['horror_n'] = 0
                doc['romance_n'] = 0
                doc['western_n'] = 0
            else:
                doc['action_adv_war_n'] = round(action_adv_war_n / total,4)
                doc['sports_n'] = round(sports_n / total,4)
                doc['family_ani_n'] = round(family_ani_n / total,4)
                doc['comedy_n'] = round(comedy_n / total,4)
                doc['mystery_drama_n'] = round(mystery_drama_n / total,4)
                doc['doc_bio_hist_n'] = round(doc_bio_hist_n / total,4)
                doc['musical_n'] = round(musical_n / total,4)
                doc['horror_n'] = round(horror_n / total,4)
                doc['romance_n'] = round(romance_n / total,4)
                doc['western_n'] = round(western_n / total,4)

            w.writerow([doc.get(col) for col in cols])
            doc = {}
        else:
            idx = line.find(':')
            if idx != -1:
              key, value = tuple([line[:idx], line[idx+1:]])
              key = key.strip().replace("/", "_").lower()
              value = value.strip()
              if key != 'review_summary' and key != 'review_text':
                doc[key] = trycast(value)
              else:
                doc[key] = value
    f.close()
