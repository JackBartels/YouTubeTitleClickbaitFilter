import lxml.html
import requests
import re

# n = 250
# (title, clickbait?) tuple list
goldStandard = [("Ending the Subscribe to Pewdiepie Meme", False),
     ("Chiitan: Last Week Tonight with John Oliver (HBO)", False),
     ("Game of Thrones | Season 8 Episode 4 | Preview (HBO)", False),
     ("21 Savage - ball w/o you", False),
     ("Game of Thrones Season 8 Episode 4 Preview Breakdown", False),
     ("Putting Weird Things In An Air Fryer (TEST)", True),
     ("Game of Thrones Season 8 Episode 3 Review and Breakdown", False),
     ("20 Things Nobody Saw Coming in Marvel Avengers Endgame", True),
     ("Avengers: Endgame - Spoiler Review", False),
     ("What To Do When Someone Parks in the Access Aisle", False),
     ("James Harden 'choked under pressure' in the Rockets' Game 1 loss - Max Kellerman | First Take", False),
     ("Game Of Thrones Season 8 Episode 3 'The Long Night' Breakdown!", False),
     ("5 Giant DIY Foods Challenge & How To Make The Best Avengers Endgame Pancake Art in 24 Hours", True),
     ("Whale filmed harassing Norwegian boats could be 'Russian weapon'", False),
     ("'Everything Is a Liability' to Kourtney Kardashian's Law Student Sister Kim", False),
     ("When Your Best Friend Exposes Your Crush To The Entire School *SO EMBARRASSING!*", True),
     ("12 Details In 'Game of Thrones' Season 8 Episode 3 You Might Have Missed", True),
     ("$50,000 Tiny House Vs. $165,000 Tiny House", True),
     ("My First Toxic Relationship", False),
     ("Game of Thrones S8 - The Night King - Ramin Djawadi (Official Video)", False),
     ("TESLA Model 3 vs BMW M3 Track Battle | Top Gear", True),
     ("Game Theory: Hard Mode is a LIE! (Sekiro Easy Mode Controversy)", True),
     ("ROCKETS vs WARRIORS | Kevin Durant Continues Stellar Scoring | Game 1", False),
     ("Turning Pencil Lead into Diamonds", True),
     ("Putting A Whole Cake In An Air Fryer (TEST)", True),
     ("Game of Thrones: Season 8 Episode 3 - Review", False),
     ("The Kinds' 'Yeh Raat' Is Mind-Blowing - World of Dance 2019 (Full Performance)", True),
     ("Real Doctor Reacts to 'Adam Ruins the Hospital'", False),
     ("Getting a signed bat from Mike Trout at Globe Life Park!", False),
     ("Devin Shares Her Sexual Assault Story - Ladylike", False),
     ("Game of Thrones Season 8 EP3 (The Long Night) Review, Critiques, Analysis", False),
     ("The UGLY TRUTH Of Owning PROPERTY WITH A VIEW", True),
     ("Macs are SLOWER than PCs. Here's why.", True),
     ("McDonald's AARP Initiative, Bumble Safety Feature & Tech-Savvy Chimp | The Daily Show", False),
     ("6 Kitchen Gadgets put to the Test - Part 45", True),
     ("My Dog Reacts to Car Wash", True),
     ("Taylor Swift - ME! (feat. Brendon Urie of Panic! At The Disco)", False),
     ("This PC wouldn't boot...you'll never guess why!", True),
     ("YouTubers React To YouTube Videos With ZERO VIEWS", True),
     ("Sharks' Brent Burns Crushes Matt Calvert, Allows Nathan MacKinnon To Score Empty-Netter", False),
     ("Do All Jubilee Employees Think The Same?", False),
     ("Q&A With Grey: Favorites Edition", False),
     ("Avengers: Endgame's Biggest Unanswered Questions", True),
     ("Homemade Vs. Fast Food: Krispy Kreme Doughnuts - Tasty", True),
     ("FaZe Clan $1,000 Basketball Trickshot Challenge", False),
     ("Man United v. Chelsea | PREMIER LEAGUE EXTENDED HIGHLIGHTS | 4/28/19 | NBC Sports", True),
     ("Ten-year-old Giorgia gets Alesha's GOLDEN BUZZER with MIND-BLOWING vocals! | Auditions | BGT 2019", True),
     ("Avengers: Endgame Pitch Meeting", False),
     ("Would You Spend $100 on Meatballs or $1 Million on a Pigeon?", True),
     ("Mozzy - Chill Phillipe (Official Video)", False),
     ("Lil Dicky - Earth (Official Music Video)", False),
     ("Offset - Cloud ft. Cardi B", False),
     ("Anything You Can Carry, I'll Pay For Challenge", False),
     ("Making My Own Starbucks Pinkity Drinkity", False),
     ("The Try Guys Make Sushi Rolls", False),
     ("All Sports Baseball Battle | Dude Perfect", False),
     ("Birdman - Cap Talk ft. YoungBoy Never Broke Again", False),
     ("Meet Bunny Our Rescue Greyhouund", False),
     ("Full Face Using Only Milani Makeup... I'm Shook!", True),
     ("Amigos (Ep. 4) | Lele Pons, Rudy Mancuso, Juanpa Zurita, Hannah Stocking & Anwar Jibawi", False),
     ("Fortnite X Avengers: Endgame Trailer", False),
     ("The Ending Of Endgame Explained", False),
     ("S2E1: 'Mercy Part II'", False),
     ("Everyday Things You NEVER KNEW The Purpose Of", True),
     ("Try Not To Eat Challenge - Disney Food #3 | People Vs. Food", False),
     ("Adam Sandler's Reaction to His Daughter Locking Eyes with Boys", True),
     ("Godzilla: King of the Monsters - Final Trailer", False),
     ("Avengers: Endgame Cast Answer 50 of the Most Googled Marvel Questions | WIRED", True),
     ("Ozuna - Baila Baila Baila (Remix) Feat. Daddy Yankee, J Balvin, Farruko, Anuel AA (Audio Oficial)", False),
     ("THE SEARCH FOR OUR NEW PET!", True),
     ("How I Really Feel About That BEL-AIR Trailer", False),
     ("Film Theory: Thanos vs Ant Man - Cracking Endgame's Biggest Meme!", False),
     ("We Built the Worlds Largest Jello Cup!", True),
     ("Did refs let Warriors get away with fouls in Game 1? | After the Buzzer | 2019 NBA Playoffs", True),
     ("Avengers: Endgame - SPOILER Talk", False),
     ("BTS (Boy With Luv) feat. Halsey' Official MV", False),
     ("Farruko, Anuel AA, Kendo Kaponi - Delincuente (Pseudo Video)", False),
     ("Avengers Endgame Review", False),
     ("Maddona, Maluma - Medellin", False),
     ("Basically Everything You Need To Know Before End Game", True),
     ("Chris Hemsworth and Scarlett Johansson Insult Each Other | CONTAINS STRONG LANGUAGE!", True),
     ("Picks 1-10: Multiple QBs, a Top 10 Trade & More! | 2019 NFL Draft", False),
     ("Everything Wrong with Spider-Man: Into the Spider-Verse", True),
     ("Ghetto Avengers | Rudy Mancuso, King Bach & Simon Rex", False),
     ("Marshmello - Light It Up ft. Tyga & Chris Brown (Official Music Video)", False),
     ("Murder Mystery | Trailer | Netflix", False),
     ("SPIDER-MAN: FAR FROM HOME - Official Trailer", True),
     ("TELLING OUR PARENTS WE'RE HAVING A BABY! (Emotional)", True),
     ("Ping Pong Trick Shots 5 | Dude Perfect", False),
     ("Kevin Gate - #Yukatan", False),
     ("Chain Restaurant Steak Taste Test", False),
     ("NERF Hide n Seek in $20,000,000 MANSION!!", True),
     ("Everything Is Better With Doodles - Doodland #29", False),
     ("Cardi B on Her Ruby Nipples and Feminism-Inspired Dress | Met Gala 2019 With Liza Koshy | Vogue", False),
     ("Binging with Babish: Good Morning Burger from The Simpsons", False),
     ("Kevin Smith Reacts to Spider-Man: Far From Home Trailer", True),
     ("How a Fire Sprinkler Works at 100,000fps - The Slow Mo Guys", False),
     ("WARRIORS vs ROCKETS | Houston Holds Serve | Game 4", False),
     ("Lady Gaga Met Gala 2019 Transformation", False),
     ("Chain Restaurant Crouton Taste Test", False),
     ("Houston Holds on at Home to Even the Series at 2-2 | NBA on TNT", False),
     ("Pop Culture Gaffes Like Starbucks Cup in 'Game of Thrones'", False),
     ("HIGHLIGHTS | Canelo Alvarez vs. Daniel Jacobs", True),
     ("Lil Nas X Goes Sneaker Shopping With Complex", False),
     ("Prince Harry And Meghan Markle Welcome 1st Child, A Boy | TODAY", False),
     ("Roman Reigns' defiance sparks a 'Wild Card Rule': Raw, May 6, 2019", False),
     ("The Kings' Final Routine is an Action Movie Live on Stage - World of Dance World Finals 2019", False),
     ("Manchester City v. Leicester City | EXTENDED HIGHLIGHTS | 5/6/19 | NBC Sports", False),
     ("Steph Curry played terrible, but doesn't deserve that much blame--Chris Broussard | NBA | UNDISPUTED", False),
     ("Pitbull x Daddy Yankee x Natti Natasha - No Lo Trates (Official Video)", False),
     ("Jimmy Talks About Adam Sandler's Ode to Chris Farley on SNL", False),
     ("Family Feud Cold Open - SNL", False),
     ("Game of Thrones | Season 8 Episode 5 | Preview (HBO)", False),
     ("The World's Largest Cyclotron", True),
     ("SZA, The Weeknd, Travis Scott - Power Is Power (Official Video)", False),
     ("Home Alone (MUSIC VIDEO) By SML", False),
     ("NBA 2K DEVELOPER TEASES BIG CHANGES IN NBA 2K20, NEW CONTACT DUNKS & INTROS", True),
     ("20 Things Only Adults Notice In The MCU", True),
     ("RESULTS: American Idol Judges Use Their SAVE - American Idol 2019 on ABC", True),
     ("Gordon Ramsay Goes Oyster Fishing In Thailand | Gordon's Great Escape", False),
     ("$8 Kitchen Knife Vs. $800 Kitchen Knife", True),
     ("30 vs 1: Dating App in Real Life", False),
     ("Is it a Good Idea to put PIZZA in a Waffle Iron?", True),
     ("Guy Fawkes vs Che Guevara. Epic Rap Battles of History.", False),
     ("Fans Control Sofie Dossi Underwater Photo Challenge **EPIC**", True),
     ("Country Horse wins Kentucky Derby after historic disqualification", False),
     ("ASSUMPTIONS ABOUT CLICK!", True),
     ("LS Fest LAS VEGAS Day 2: Leroy Releases all the BALD EAGLES on the Dyno!", False),
     ("BREAKING OUR DIETS WITH EPIC CHEAT MEAL! ft GABBIE HANNA", True),
     ("46th Daytime Emmys", False),
     ("Mustang GT Catback Exhaust Install!", False),
     ("Disney's Aladdin - 'A Whole New World' Film Clip", False),
     ("WE CRASHED HIS DATE WITH 100 SUBSCRIBERS", True),
     ("RELATABLE SITUATIONS ANYONE CAN RECOGNIZE || Funny Moments by 123 GO!", True),
     ("Ni Bien Ni Mal - Bad Bunny ( Video Oficial)", False),
     ("Taste Testing the Latest 'Food Trend' Products", False),
     ("Sonic The Hedgehog (2019) - Official Trailer - Paramount Pictures", False),
     ("Iggy Azalea - Started (Official Music Video)", False),
     ("Blueface Stop Cappin (Official Music Video)", False),
     ("Kentucky Derby 2019 (FULL RACE) ends in historic controversial finish | NBC Sports", False),
     ("Last To Sink Wins $10,000 - Challenge", False),
     ("Choosing My Wedding Dress", False),
     ("Jealous, Cake By The Ocean, Sucker Medley (Live From The Billboard Music Awards / 2019)", False),
     ("Camping Overnight With No Technology", False),
     ("Tom Brady Helps Jimmy Kimmel Vandalize Matt Damon's House", False),
     ("Ariana Grande - 7 rings (Live From The Billboard Music Awards / 2019)", False),
     ("Halsey - Without Me (Live From the Billboard Music Awards)", False),
     ("Letting The Person in FRONT of Me Decide What I Eat!", True),
     ("Billie Eilish Takes 'The Office' Quiz With Rainn Wilson | Billboard", False),
     ("Shawn Mendes - If I Can't Have You", False),
     ("2 Week Bunny Update", False),
     ("Birdman - Cap Talk ft. YoungBoy Never Broke Again", False),
     ("How Hard Can You Hit a Golf Ball? (at 100,000 FPS) - Smarter Every Day 2016", True),
     ("A Smith Family COACHELLA", False),
     ("Will It Slime?", False),
     ("The Puzzling Disappearance of Walter Collins", False),
     ("Offset - Clout ft. Cardi B", False),
     ("Karol G - Ocean (Video Oficial)", False),
     ("Sonic The Hedgehog Improved Trailer", False),
     ("Seth Rogen and Charlize Theron Play Truth or Dab | Hot Ones", False),
     ("Saying Goodbye To Our House Forever...WE'RE OFFICIALLY MOVED IN!!!", True),
     ("'I sacrified my talent' playing with Kyrie Irving and Gordon Hayward - Terry Rozier | First Take", False),
     ("Official Teaser: Disney's Maleficent: Mistress of Evil - In Theaters October 18!", False),
     ("OnePlus 7 Pro Review: Silly Fast!", False),
     ("OUR EMPTY HOUSE TOUR!", True),
     ("THE PRINCE FAMILY - NOW WE UP (Official Music Video) TRAILER!!!", True),
     ("Leaving Things In Windex For A Month", True),
     ("17 Details In 'Game of Thrones' Season 8 Episode 5 You Might Have Missed", True),
     ("OnePlus 7 Pro Unboxing - It's ALL SCREEN", False),
     ("Working Weird Craigslist Jobs to Earn $965 for New York City Rent", True),
     ("Binging with Babish: Teddy Brulee from Bob's Burgers", False),
     ("Here's Why the 2020 Toyota Supra Could Be Better", True),
     ("i'm almost done with high school...+haul", False),
     ("Underwater OnePlus 7 Pro Review", False),
     ("Game of Thrones | Season 8 Episode 6 | Preview (HBO)", False),
     ("MIDSOMMAR | Official Trailer HD | A24", False),
     ("'Superman dive' at finishing line gives university athlete dramatic win in 400m hurdles", False),
     ("Kawhi made the luckiest shot in history of the NBA Playoffs -- Skip Bayless | NBA | UNDISPUTED", False),
     ("Chris and Andy Try to Make the Perfect Pizza Toppings | Making Perfect: Episode 4 | Bon Appetit", False),
     ("How This Flower Saved Me", True),
     ("Why are people so mad at Game of Thrones?", False),
     ("This Adapter Will Destroy Your Car", True),
     ("NIGAHIGA VS SIDEMEN - THE ULTIMATE CHALLENGE", True),
     ("Game of Thrones: Season 8 Episode 5 - Review", False),
     ("IF TV SHOWS WERE REAL 4", True),
     ("The Game Shows Off His Bulletproof Sneaker Colleciton On Complex Closets", False),
     ("The Side Effects of Vaccines - How High is the Risk?", False),
     ("FOOD ART CHALLENGE & How To Make the Best Avengers Pokemon Detective Pikachu Pancake Art", True),
     ("Weekend Update: Pete Davidson on Living with His Mom - SNL", False),
     ("J.R. Smith's NBA Finals blunder deserves a deep rewind | Warriors vs Cavaliers 2018", False),
     ("WORLD'S MOST FAMOUS MAGIC TRICKS REVEALED!", True),
     ("Rebuilding A Wrecked Lamborghini Huracan Part 22", False),
     ("MUST TRY Singapore CHEAP EATS! Hawker Street Food Tour of Singapore", True),
     ("Jarret Hurd vs Julian WIlliams full fight | HIGHLIGHTS | PBC ON FOX", False),
     ("How Julian Newman Prepared To Play LAMELO BALL! Jaden Newman Has A CRUSH On Melo!?", True),
     ("UFC 237: Rose Namajunas post-fight interview", False),
     ("Jonas Brothers - Cool, Burnin Up (Live From Saturday Night Live / 2019)", False),
     ("Foreign Mothers | Anwar Jibawi & Rudy Mancuso", False),
     ("Destroying Giant Stress Balls (Satisfying)", True),
     ("10 TV And Movie Mistakes You Won't Believe You Missed | Find The Flaws", True),
     ("Soltera Remix - Lunay X Daddy Yankee X Bad Bunny ( Video Oficial )", False),
     ("The Try Guys Try 13 Future Technologies At Google", True),
     ("6 Strange Ice Cream Scoops Put to the Test!", True),
     ("We Try On Wedding Dresses - Ladylike", False),
     ("How Safe Is A Duct Tape Ladder?", False),
     ("Why Are 96,000,000 Black Balls on This Reservoir?", True),
     ("Sansa vs. Daenerys: Sophie Turner Blames Emilia Clarke for Game of Thrones Coffee Cup-gate", False),
     ("Dwight Schrute Vs The World - The Office US", False),
     ("IT CHAPTER TWO - Official Teaser Trailer [HD]", True),
     ("Spending 24 Hours In A City With No Laws", False),
     ("Ed Sheeran & Justin Bieber - I Don't Care [Official Lyric Video]", False),
     ("Mike D'Antoni is in a 'world of trouble', could be fired by the Rockets = Stephen A. | First Take", False),
     ("Quando Rondo - Imperfect Flower (Official Video)", False),
     ("Hot Cold Food Vs. Cold Hot Food Taste Test", False),
     ("Kourtney Kardashian Reveals Kim's Baby Bombshell to Kris Jenner", True),
     ("ZAYN, Zhavia Ward - A Whole New World (End Title) (From 'Aladdin'/Official Video)", False),
     ("The Curious Death of Vincent Van Gogh", False),
     ("WARRIORS vs ROCKETS | Stephen Curry Drops 33 Points in the 2nd Half | Game 6", False),
     ("We Try Our Mom's Morning Routines - Ladylike", False),
     ("Kim Kardashian West Gets Fitted for Her Waist-Snatching Met Gala Look | Vogue", False),
     ("Luke Combs - Beer Never Broke My Heart", False),
     ("Watchmen | Official Tease | HBO", False),
     ("Solving a $10,000 Puzzle Box - Level 10 (One of a kind)", False),
     ("This Low Budget Movie Is a Disaster", True),
     ("Ven Y Hazlo Tu - Nicky Jam x J Balvin x Anuel AA x Arcangel | Video Official", False),
     ("Paulo Londra - Solo Pienso en Ti ft. De La Ghetto, Justin Quiles (Official Video)", False),
     ("Destiny 2: Forsaken - Season of Opulence Trailer", False),
     ("Lance Stewart - LOST (OFFICIAL MUSIC VIDEO)", False),
     ("Brock Lesnar learns an important Money in the Bank detail: Raw, May 27, 2019", False),
     ("RIDDLES You Must Solve To Survive", True),
     ("The AirPods Alternative You've Been Waiting For", True),
     ("FaZe Clan Arm Wrestling Challenge", False),
     ("As Seen On TV Automobile Gadgets Tested!", True),
     ("BEST Self Alley-Oop Dunks | $50,000 Dunk Contest", True),
     ("Our TINY HOME on the Ocean Ep. 199", False),
     ("I need to buy AMD stock. NOW.", True),
     ("2020 iPhones Excite! Touch ID 3, Best iOS 13 Concept & SE 2!", False),
     ("MY FIRST PRACTICE AS A PRO FOOTBALL PLAYER..(HARDER THAN I THOUGHT)", True),
     ("I Spent A Day With A Teen Mom", False),
     ("Cody explains the Triple H reference in his DoN entrance, Jon Moxley, his match with Dustin", False),
     ("Most Amazing COINCIDENCES You Won't Believe !", True),
     ("LIVING MY LAST 24 HOURS WITH $40,000", True),
     ("This Happens when you Boil ORGANIC Apple Juice", True),
     ("IndyCar Indianapolis 500 2019 | EXTENDED HIGHLIGHTS | 5/26/19 | NBC Sports", False),
     ("No one asked but I found Mortal Kombat's best cuddler | Unraveled", False),
     ("8 Putties You Won't Be Able to Put Down", True),
     ("SIDEMEN LEARN TO DANCE ft. JABBAWOCKEEZ", True),
     ("2019 Monaco Grand Prix: Race Highlights", False),
     ("Do Teens Know Their Parents' Favorite 90s Cartoon Themes? | React: Do They Know It?", True),
     ("Kevin Gates - I Got That Dope", False)]

# Generates Testing List
def genTest():
    # Fetches YouTube Trending HTML and stores it in a string
    trending_req = requests.get("https://www.youtube.com/feed/trending")
    trending_html = trending_req.text


    # Utilizes regex to create a list of titles found on the page
    titleListUnf = re.findall(r"(?<=title=\").+?(?=\")", trending_html)


    # YouTube button titles to filter out; may use id="video-title" specifier in future
    buttonTitles = ["Queue", "Verified", "Loading icon", "Watch later", "YouTube home",
                    "YouTube Video Search", "YouTube Home", "Upload", "Search", "Home",
                    "Trending", "History", "Get YouTube Premium", "Get YouTube TV",
                    "Music", "Sports", "Gaming", "Movies", "TV Shows", "News", "Live",
                    "Spotlight", "360° Video", "Browse channels", "__TITLE__",
                    "Previous video", "Play", "Pause", "Next video", "stop"]

    titleList = []

    # Unfiltered (titleListUnf) -> Filtered (titleList)
    for title in titleListUnf:
        if title not in buttonTitles and "http" not in title:
            titleList.append(title)

    return titleList

# Keyword Filter
def keywordFilter(titleList, verbose):
    filteredList = []

    for title in titleList:
        clickbait = False

        # Keywords
        if not(re.search(r"biggest", title, re.IGNORECASE) == None):
            clickbait = True
        if not(re.search(r"largest", title, re.IGNORECASE) == None):
            clickbait = True
        if not(re.search(r"mind([- ])blowing", title, re.IGNORECASE) == None):
            clickbait = True
        if not(re.search(r"worst", title, re.IGNORECASE) == None):
            clickbait = True
        if not(re.search(r"amazing", title, re.IGNORECASE) == None):
            clickbait = True
        if not(re.search(r"never", title, re.IGNORECASE) == None):
            clickbait = True
        if not(re.search(r"click", title, re.IGNORECASE) == None):
            clickbait = True
        if not(re.search(r"woah", title, re.IGNORECASE) == None):
            clickbait = True
        if not(re.search(r"wow", title, re.IGNORECASE) == None):
            clickbait = True
        if not(re.search(r"surprising", title, re.IGNORECASE) == None):
            clickbait = True
        if not(re.search(r"omg", title, re.IGNORECASE) == None):
            clickbait = True
        if not(re.search(r"crazy", title, re.IGNORECASE) == None):
            clickbait = True

        # Verbose mode prints test titles alongside whether or not they are clickbait
        if verbose:
            if clickbait:
                print("Clickbait: ", title)
            else:
                print("Not clickbait: ", title)

        filteredList.append((title, clickbait))

    return filteredList

# Phrase Filter
def phraseFilter(titleList, verbose):
    filteredList = []

    for title in titleList:
        clickbait = False

        # Phrases
        if not(re.search(r"here.*s why", title, re.IGNORECASE) == None):
            clickbait = True
        if not(re.search(r"you never knew", title, re.IGNORECASE) == None):
            clickbait = True
        if not(re.search(r"won.*t believe", title, re.IGNORECASE) == None):
            clickbait = True
        if not(re.search(r"weird trick", title, re.IGNORECASE) == None):
            clickbait = True
        if not(re.search(r"see this", title, re.IGNORECASE) == None):
            clickbait = True
        if not(re.search(r"watch this", title, re.IGNORECASE) == None):
            clickbait = True
        if not(re.search(r"find out", title, re.IGNORECASE) == None):
            clickbait = True
        if not(re.search(r"life changing", title, re.IGNORECASE) == None):
            clickbait = True
        if not(re.search(r"need to see", title, re.IGNORECASE) == None):
            clickbait = True
        if not(re.search(r"will make you", title, re.IGNORECASE) == None):
            clickbait = True
        if not(re.search(r"this is what happens", title, re.IGNORECASE) == None):
            clickbait = True
        if not(re.search(r"oh my god", title, re.IGNORECASE) == None):
            clickbait = True
        if not(re.search(r"this is nuts", title, re.IGNORECASE) == None):
            clickbait = True

        # Verbose mode prints test titles alongside whether or not they are clickbait
        if verbose:
            if clickbait:
                print("Clickbait: ", title)
            else:
                print("Not clickbait: ", title)

        filteredList.append((title, clickbait))

    return filteredList

# Format Filter
def formatFilter(titleList, verbose):
    filteredList = []

    for title in titleList:
        clickbait = False

        # Formats
        if not(re.search(r"^Guess .*", title, re.IGNORECASE) == None):
            clickbait = True
        if not(re.search(r"^[0-9]+ (?!in ).*", title, re.IGNORECASE) == None):
            clickbait = True
        if not(re.search(r"^(?<!I )[A-Z]+ [(A-Z|0-9)]+ .*", title) == None):
            clickbait = True
        if not(re.search(r".*\*\*.*", title, re.IGNORECASE) == None):
            clickbait = True
        if not(re.search(r".*\?!+.*", title, re.IGNORECASE) == None):
            clickbait = True
        if not(re.search(r".*!\?+.*", title, re.IGNORECASE) == None):
            clickbait = True
        if not(re.search(r".*\?{3,}.*", title, re.IGNORECASE) == None):
            clickbait = True
        if not(re.search(r".*\!{3,}.*", title, re.IGNORECASE) == None):
            clickbait = True
        if not(re.search(r".*[A-Z]+ [A-Z]+ [A-Z]+.*", title) == None):
            clickbait = True

        # Verbose mode prints test titles alongside whether or not they are clickbait
        if verbose:
            if clickbait:
                print("Clickbait: ", title)
            else:
                print("Not clickbait: ", title)

        filteredList.append((title, clickbait))

    return filteredList

# Combo Filter
def comboFilter(titleList, verbose):
    filteredList = []

    for title in titleList:
        clickbait = False

        # Keywords
        if not(re.search(r"biggest", title, re.IGNORECASE) == None):
            clickbait = True
        if not(re.search(r"largest", title, re.IGNORECASE) == None):
            clickbait = True
        if not(re.search(r"mind([- ])blowing", title, re.IGNORECASE) == None):
            clickbait = True
        if not(re.search(r"worst", title, re.IGNORECASE) == None):
            clickbait = True
        if not(re.search(r"amazing", title, re.IGNORECASE) == None):
            clickbait = True
        if not(re.search(r"never", title, re.IGNORECASE) == None):
            clickbait = True
        if not(re.search(r"click", title, re.IGNORECASE) == None):
            clickbait = True
        if not(re.search(r"woah", title, re.IGNORECASE) == None):
            clickbait = True
        if not(re.search(r"wow", title, re.IGNORECASE) == None):
            clickbait = True
        if not(re.search(r"surprising", title, re.IGNORECASE) == None):
            clickbait = True
        if not(re.search(r"omg", title, re.IGNORECASE) == None):
            clickbait = True
        if not(re.search(r"crazy", title, re.IGNORECASE) == None):
            clickbait = True

        # Phrases
        if not(re.search(r"here.*s why", title, re.IGNORECASE) == None):
            clickbait = True
        if not(re.search(r"you never knew", title, re.IGNORECASE) == None):
            clickbait = True
        if not(re.search(r"won.*t believe", title, re.IGNORECASE) == None):
            clickbait = True
        if not(re.search(r"weird trick", title, re.IGNORECASE) == None):
            clickbait = True
        if not(re.search(r"see this", title, re.IGNORECASE) == None):
            clickbait = True
        if not(re.search(r"watch this", title, re.IGNORECASE) == None):
            clickbait = True
        if not(re.search(r"find out", title, re.IGNORECASE) == None):
            clickbait = True
        if not(re.search(r"life changing", title, re.IGNORECASE) == None):
            clickbait = True
        if not(re.search(r"need to see", title, re.IGNORECASE) == None):
            clickbait = True
        if not(re.search(r"will make you", title, re.IGNORECASE) == None):
            clickbait = True
        if not(re.search(r"this is what happens", title, re.IGNORECASE) == None):
            clickbait = True
        if not(re.search(r"oh my god", title, re.IGNORECASE) == None):
            clickbait = True
        if not(re.search(r"this is nuts", title, re.IGNORECASE) == None):
            clickbait = True

        # Formats
        if not(re.search(r"^Guess .*", title, re.IGNORECASE) == None):
            clickbait = True
        if not(re.search(r"^[0-9]+ (?!in ).*", title, re.IGNORECASE) == None):
            clickbait = True
        if not(re.search(r"^(?<!I )[A-Z]+ [(A-Z|0-9)]+ .*", title) == None):
            clickbait = True
        if not(re.search(r".*\*\*.*", title, re.IGNORECASE) == None):
            clickbait = True
        if not(re.search(r".*\?!+.*", title, re.IGNORECASE) == None):
            clickbait = True
        if not(re.search(r".*!\?+.*", title, re.IGNORECASE) == None):
            clickbait = True
        if not(re.search(r".*\?{3,}.*", title, re.IGNORECASE) == None):
            clickbait = True
        if not(re.search(r".*\!{3,}.*", title, re.IGNORECASE) == None):
            clickbait = True
        if not(re.search(r".*[A-Z]+ [A-Z]+ [A-Z]+.*", title) == None):
            clickbait = True

        # Verbose mode prints test titles alongside whether or not they are clickbait
        if verbose:
            if clickbait:
                print("Clickbait: ", title)
            else:
                print("Not clickbait: ", title)

        filteredList.append((title, clickbait))

    return filteredList

goldTitles = []

for tuple in goldStandard:
    goldTitles.append(tuple[0]) 

goldEvalKeyList = keywordFilter(goldTitles, False)
goldEvalPhrList = phraseFilter(goldTitles, False)
goldEvalForList = formatFilter(goldTitles, False)
goldEvalCmbList = comboFilter(goldTitles, False)

def evaluate(progList, goldList):
    truePos = 0
    trueNeg = 0
    falsePos = 0
    falseNeg = 0

    size = 250
    recall = 0.0
    precision = 0.0
    f1score = 0.0
	
    for idx in range(size):
        if (progList[idx][1] == goldList[idx][1]) and (progList[idx][1] == True):
            truePos += 1
        if (progList[idx][1] == goldList[idx][1]) and (progList[idx][1] == False):
            trueNeg += 1
        if (progList[idx][1] != goldList[idx][1]) and (goldList[idx][1] == True):
            falseNeg += 1
        if (progList[idx][1] != goldList[idx][1]) and (goldList[idx][1] == False):
            falsePos += 1
				
    print(truePos)
    print(falsePos)
    print(trueNeg)
    print(falseNeg)

    recall = truePos / (truePos + falseNeg)
    precision = truePos / (truePos + falsePos)
    f1score = 2 * (precision * recall) / (precision + recall)

    print("Recall: ", recall)
    print("Precision: ", precision)
    print("F1 Score: ", f1score)
	
print("\nKeywords Only:")
evaluate(goldEvalKeyList, goldStandard)
print("\nPhrases Only:")
evaluate(goldEvalPhrList, goldStandard)
print("\nFormats Only:")
evaluate(goldEvalForList, goldStandard)
print("\nAll Combined:")
evaluate(goldEvalCmbList, goldStandard)
