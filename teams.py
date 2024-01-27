import random

def play_game(team1, team2):
    '''get result from one game'''
    
    t1_score = random.randrange(45,85)
    t2_score = random.randrange(45,85)
    extra = " "
    
    n_ot = 1
    while t1_score == t2_score:
        t1_score += random.randrange(5,20)
        t2_score += random.randrange(5,20)
        
        if n_ot == 1:
            extra = "OT"
        else:
            extra = f"{n_ot}OT"
            
        n_ot += 1
    
    return t1_score, t2_score, extra


teams = '''Abilene Christian
Air Force
Akron
Alabama
Alabama A&M
Alabama State
Albany (NY)
Alcorn State
Allegheny Gators
American
Amherst Lord Jeffs
Appalachian State
Arizona (9)
Arizona State
Arkansas
Arkansas State
Arkansas-Pine Bluff
Armstrong Pirates
Army
Auburn (8)
Augusta State Jaguars
Augustana (IL) Vikings
Austin Peay
Baker University Wildcats
Baldwin-Wallace Yellow Jackets
Ball State
Baltimore Super Bees
Baylor (15)
Bellarmine
Belmont
Beloit Buccaneers
Bethune-Cookman
Binghamton
Birmingham-Southern Panthers
Bloomsburg Huskies
Boise State
Boston College
Boston University
Bowling Green State
Bradley
Brigham Young (21)
Brigham Young College
Brooklyn Bulldogs
Brown
Bryant
Bucknell
Buffalo
Butler
Cal Poly
Cal State Bakersfield
Cal State Fullerton
Cal State Los Angeles Golden Eagles
Cal State Northridge
California
California Baptist
Campbell
Canisius
Canterbury College
Carleton College Knights
Carnegie Mellon Tartans
Case Western Reserve Spartans
Catholic Cardinals
Centenary (LA) Gents
Central Arkansas
Central Connecticut State
Central Florida
Central Michigan
Central Missouri Mules
Central Pennsylvania College Knights
Centre (KY) Colonels
Charleston Southern
Charlotte
Chattanooga
Cheyenne Business College
Chicago Maroons
Chicago State
Cincinnati
City College of New York Beavers
Clemson
Cleveland State
Coastal Carolina
Colgate
College of Charleston
College of New Jersey Lions
Colorado
Colorado College Tigers
Colorado School of Mines Orediggers
Colorado State (24)
Columbia
Concordia Seminary Preachers
Connecticut (1)
Coppin State
Cornell
Cotner College
Creighton (17)
Cumberland
Dakota Wesleyan Tigers
Dartmouth
Davidson
Dayton (16)
Delaware
Delaware State
Denison Big Red
Denver
DePaul
DePauw Tigers
Detroit Mercy
Dickinson College Red Devils
Drake
Drexel
Duke (12)
Duquesne
East Carolina
East Central Tigers
East Tennessee State
Eastern Illinois
Eastern Kentucky
Eastern Michigan
Eastern Washington
Elon
Emporia State Hornets
Ensign College
Evansville
Fairfield
Fairleigh Dickinson
Florida
Florida A&M
Florida Atlantic (22)
Florida Gulf Coast
Florida International
Florida State
Fordham
Franklin Grizzlies
Fresno State
Furman
Gardner-Webb
Geneva Golden Tornadoes
George Mason
George Washington
Georgetown
Georgia
Georgia Southern
Georgia State
Georgia Tech
Gettysburg Bullets
Gonzaga
Grambling
Grand Canyon
Green Bay
Grinnell Pioneers
Grove City Wolverines
Hamline Pipers
Hampton
Hardin-Simmons Cowboys
Hartford Hawks
Harvard
Haskell (KS) Fighting Indians
Hawaii
High Point
Hiram Terriers
Hofstra
Holy Cross
Hope Flying Dutchmen
Houston (4)
Houston Christian
Howard
Idaho
Idaho State
Illinois (10)
Illinois State
Illinois Wesleyan Titans
Illinois-Chicago
Incarnate Word
Indiana
Indiana State
Iona
Iowa
Iowa State (23)
IUPUI
Jackson State
Jacksonville
Jacksonville State
James Madison
John Carroll Blue Streaks
Kalamazoo Hornets
Kansas (7)
Kansas City
Kansas State
Kennesaw State
Kent State
Kentucky (6)
Kentucky Wesleyan Panthers
La Salle
Lafayette
Lake Forest Foresters
Lamar
Lawrence Tech
Le Moyne
Lehigh
Lewis Flyers
Liberty
Lindenwood
Lipscomb
Little Rock
Long Beach State
Long Island University
Longwood
Louisiana
Louisiana State
Louisiana Tech
Louisiana-Monroe
Louisville
Loyola (IL)
Loyola (LA) Wolfpack
Loyola (MD)
Loyola Marymount
Macalester Scots
Maine
Manchester Spartans
Manhattan
Marietta Pioneers
Marist
Marquette (14)
Marshall
Maryland
Maryland-Baltimore County
Maryland-Eastern Shore
Massachusetts
Massachusetts Institute of Technology Engineers
Massachusetts-Lowell
McNeese State
Memphis (19)
Mercer
Merchant Marine Mariners
Merrimack
Miami (FL)
Miami (OH)
Michigan
Michigan State
Middle Tennessee
Millikin Big Blue
Millsaps Majors
Milwaukee
Minnesota
Minnesota A&M Aggies
Mississippi
Mississippi State
Mississippi Valley State
Missouri
Missouri State
Monmouth
Montana
Montana State
Morehead State
Morgan State
Morris Brown Wolverines
Mount St. Mary's
Mount Union Purple Raiders
Muhlenberg Mules
Murray State
Muskingum Fighting Muskies
Navy
NC State
Nebraska
Nebraska Wesleyan Prairie Wolves
Nevada
Nevada-Las Vegas
New Hampshire
New Mexico (25)
New Mexico State
New Orleans
New York University Violets
Newberry Wolves
Niagara
Nicholls State
NJIT
Norfolk State
North Alabama
North Carolina (3)
North Carolina A&T
North Carolina Central
North Central Cardinals
North Dakota
North Dakota State
North Florida
North Texas
Northeastern
Northeastern Illinois Golden Eagles
Northern Arizona
Northern Colorado
Northern Illinois
Northern Iowa
Northern Kentucky
Northwest Missouri State Bearcats
Northwestern
Northwestern State
Notre Dame
Oakland
Oberlin Yeomen
Ohio
Ohio State
Ohio Wesleyan Battling Bishops
Oklahoma (11)
Oklahoma City Chiefs
Oklahoma State
Old Dominion
Omaha
Oral Roberts
Oregon
Oregon State
Pacific
Penn State
Pennsylvania
Pepperdine
Phillips Haymakers
Pittsburg State Gorillas
Pittsburgh
Portland
Portland State
Prairie View
Pratt Institute Cannoneers
Presbyterian
Princeton
Providence
Purdue (2)
Purdue Fort Wayne
Queens (NC)
Quinnipiac
Radford
Regis (CO) Rangers
Rensselaer Engineers
Rhode Island
Rice
Richmond
Rider
Ripon Red Hawks
Roanoke Maroons
Robert Morris
Rochester (NY) Yellowjackets
Rose-Hulman Fightin' Engineers
Rutgers
Sacramento State
Sacred Heart
Saint Francis (PA)
Saint Joseph's
Saint Louis
Saint Mary's (CA)
Saint Peter's
Sam Houston
Samford
San Diego
San Diego State
San Francisco
San Jose State
Santa Clara
Savage School of Physical Education
Savannah State Tigers
Scranton Royals
Seattle
Seton Hall
Sewanee Tigers
Siena
South Alabama
South Carolina
South Carolina State
South Carolina Upstate
South Dakota
South Dakota State
South Florida
Southeast Missouri State
Southeastern Louisiana
Southern
Southern California
Southern Illinois
Southern Illinois-Edwardsville
Southern Indiana
Southern Methodist
Southern Mississippi
Southern Utah
Southwestern (KS) Moundbuilders
Southwestern (TX) Pirates
Springfield Pride
St. Bonaventure
St. Francis (NY) Terriers
St. John's (NY)
St. John's College (OH)
St. Lawrence Saints
St. Thomas
Stanford
Stephen F. Austin
Stetson
Stevens Institute Ducks
Stonehill
Stony Brook
SUNY-Potsdam Bears
Swarthmore Garnet
Syracuse
Tarleton State
TCU
Temple
Tennessee (5)
Tennessee State
Tennessee Tech
Tennessee-Martin
Texas
Texas A&M
Texas A&M-Commerce
Texas A&M-Corpus Christi
Texas Southern
Texas State
Texas Tech (20)
Texas Wesleyan Rams
Texas-Rio Grande Valley
The Citadel
Toledo
Towson
Trinity (CT) Bantams
Trinity (TX) Tigers
Troy
Tulane
Tulsa
U.S. International Gulls
UAB
UC Davis
UC Irvine
UC Riverside
UC San Diego
UC Santa Barbara
UCLA
UNC Asheville
UNC Greensboro
UNC Wilmington
Union (NY) Dutchmen
UT Arlington
Utah
Utah State (18)
Utah Tech
Utah Valley
UTEP
Utica Pioneers
UTSA
Valparaiso
Vanderbilt
Vermont
Villanova
Virginia
Virginia Commonwealth
Virginia Military Institute
Virginia Tech
Wabash Little Giants
Wagner
Wake Forest
Washburn Ichabods
Washington
Washington & Jefferson Presidents
Washington & Lee Generals
Washington (MO) Bears
Washington College Shoremen
Washington State
Wayne State (MI) Warriors
Weber State
Wesleyan (CT) Cardinals
West Chester Golden Rams
West Texas A&M Buffaloes
West Virginia
Western Carolina
Western Colorado Mountaineers
Western Illinois
Western Kentucky
Western Michigan
Westminster (MO) Blue Jays
Westminster (PA) Titans
Wheaton (IL) Thunder
Whittier Poets
Wichita State
Widener Pride
William & Mary
Williams Ephs
Winthrop
Wisconsin (13)
Wisconsin-Stevens Point Pointers
Wisconsin-Superior Yellowjackets
Wittenberg Tigers
Wofford
Wooster Fighting Scots
WPI Engineers
Wright State
Wyoming
Xavier
Yale
Youngstown State'''

teams = [t.strip() for t in teams.split("\n")]
