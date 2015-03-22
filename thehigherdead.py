# First we have to import helper modules
import random
import tweepy

# Here we tell the program how to talk to Twitter
# Replace the keys below with the real keys, keeping them in single quotation marks
auth = tweepy.OAuthHandler('consumerkey', 'consumersecret')
auth.set_access_token('oauthkey', 'oauthsecret')
api = tweepy.API(auth)

# Next we set up arrays (lists) of the words
words1 = ['The','Our','This','Uni President says:','Chancellor says:','Provost says:','Edupreneur says:','Black turtleneck says:','News from SXSW:','Pearson says:','NYT says:','Chronicle of Higher Ed says:','Vice-Provost for Spinoff-o-vation says:','Wall Street says:','Tomorrow\'s','Ass. Dean says:']

words2 = ['global','nimble','competent','digital','fluid','ed-tech','efficient','adaptable','dynamic','mobile','online','Gatesean','networked','entrepreneurial','streamlined','flexible','responsive','synergy']

words3 = ['21st century','institution','degree','badge','MOOC','mooctopia','marketplace','stakeholder','credential','platform','business model','market forces','revenue stream','workforce','digital native','brick and mortar','TEDxCampus']

words4 = ['requires','disrupts','innovates','disruptovates','innorupts','flex-o-vates','efficienates','mobilizes','edumates','gamechanges','decouples','breaks up credit hour','monetizes','dynamicifies','gamifies','incentivizes','knowledgizes','streamlines','storifies','synergizifies']

words5 = ['flexibility','status quo','competency','tradition by','classrooms','tomorrow','tools','Friedman','accountability','administration','paradigms','networked','eduvation','course delivery','market share','badges','assessment','outcomes']

words6 = ['blaarghh','snurfle','yumzh','morglepht','gadurgle','sssukbloood','murdgleztfh']

words7 = ['grrrum','glbugh','kablargle','blahserrr','splugherm','ughhhbalung','studentzzzz']

words8 = ['efficienceeeees','disruptsssssss','compentencyyyyy','innovationnnnn','Mooooooooc','businessssss','efficiencyyyy','accountabilityyyy','dynamismmm','e-text-booksssss','Think-tannnnnnk','student loanssss']

words9 = ['brainzzz','promote meeeee','buy my boooook','pay me consultant feeeeeeees']

# Now we select a random item from each array
word1 = random.choice(words1)
word2 = random.choice(words2)
word3 = random.choice(words3)
word4 = random.choice(words4)
word5 = random.choice(words5)
word6 = random.choice(words6)
word7 = random.choice(words7)
word8 = random.choice(words8)
word9 = random.choice(words9)

# Let's tie it all together. Note the ' ' which are the spaces between words
zombieReform = word1 + ' ' + word2 + ' ' + word3 + ' ' + word4 + ' ' + word5 + ' ' + word6 + ' ' + word7 + ' ' + word8 + ' ' + word9

# Print out the statement, plus the length of the statement (just to test that it's under 140 characters)
print zombieReform
print len(zombieReform)

# Uncomment this next line to actually post
#api.update_status(zombieReform)
