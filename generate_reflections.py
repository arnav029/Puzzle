import json
from datetime import date, timedelta
import random

# --- CONFIGURATION ---
START_DATE = date(2025, 12, 28)
END_DATE = date(2026, 6, 30)
OUTPUT_FILE = "reflections.json"

# --- THE DEEP REFLECTION BANK ---
# content inspired by Naval, Stoicism, Psychology, and Career Introspection
reflection_bank = [
    {
        "reflection": "If someone asked you, 'What do you bring to the table that an AI cannot do?', what would you say?",
        "perspective": "AI provides answers; humans provide questions. AI has logic; humans have taste. Your value is no longer in your labor, but in your judgment and your ability to care about the outcome."
    },
    {
        "reflection": "If you could not tell a single person about your achievements, would you still chase the same goals?",
        "perspective": "If the applause stops, does the performance still matter? Build a life that feels good on the inside, not just one that looks good on the outside."
    },
    {
        "reflection": "Who are you spending time with out of habit, rather than growth?",
        "perspective": "Naval Ravikant says: 'Play long-term games with long-term people.' If you cannot see a future with them, you are delaying your own evolution by staying in the past."
    },
    {
        "reflection": "What is something you are 'waiting' to do until you feel 'ready'?",
        "perspective": "Readiness is a myth. You do not think your way into a new way of acting; you act your way into a new way of thinking. Start before you are ready."
    },
    {
        "reflection": "If you met your 10-year-old self today, would they be proud of you, or confused?",
        "perspective": "Do not judge yourself through the eyes of a child who didn't know how hard the world is. Be proud not of the trophy, but of the survival."
    },
    {
        "reflection": "Are you productive, or are you just busy?",
        "perspective": "Direction is more important than speed. Many people are driving fast, but they are driving in circles. Stop and look at the map."
    },
    {
        "reflection": "What is the most uncomfortable truth you are currently avoiding?",
        "perspective": "The cave you fear to enter holds the treasure you seek. The thing you are avoiding is likely the exact thing you need to do next."
    },
    {
        "reflection": "How much of your anxiety is actually just an imagination of a future that hasn't happened?",
        "perspective": "Seneca said: 'We suffer more often in imagination than in reality.' Return to the present. The problem is rarely here; it is usually in your head."
    },
    {
        "reflection": "If money was no object, how would you spend your days?",
        "perspective": "The gap between that life and your current life is not just money—it is fear. You can likely afford to do 10% of that dream life today, but you are afraid to start."
    },
    {
        "reflection": "Which of your 'needs' are actually just 'wants' disguised by society?",
        "perspective": "Desire is a contract you make with yourself to be unhappy until you get what you want. Minimize your desires, and you maximize your freedom."
    },
    {
        "reflection": "When was the last time you changed your mind about something important?",
        "perspective": "A strong mind is not one that is fixed, but one that is fluid. If you haven't changed your mind recently, you aren't learning; you're just defending."
    },
    {
        "reflection": "Are you acting out of love, or out of a fear of being alone?",
        "perspective": "Solitude is dangerous to a person who has not made friends with themselves. Fix the relationship with you, and the relationships with others will heal."
    },
    {
        "reflection": "What are you holding onto that is already gone?",
        "perspective": "You cannot start the next chapter of your life if you keep re-reading the last one. Let the dead leaves fall so the new ones can grow."
    },
    {
        "reflection": "If today was the last day of your life, would you want to do what you are about to do today?",
        "perspective": "Steve Jobs asked this daily. If the answer is 'No' for too many days in a row, you know you need to change something."
    },
    {
        "reflection": "What is a 'failure' from your past that actually set you up for success?",
        "perspective": "A failure is only a failure if you stop. Otherwise, it is just data. You are not defined by the fall, but by the bounce."
    },
    {
        "reflection": "How much 'news' did you consume today, and how much of it actually impacted your life?",
        "perspective": "Most news is noise designed to sell your attention. Guard your attention like it is your bank account, because it is more valuable."
    },
    {
        "reflection": "Who in your life drains your energy, and why do you let them?",
        "perspective": "You are the average of the five people you spend the most time with. Choose carefully. It is better to be alone than to be weighed down."
    },
    {
        "reflection": "What is the smallest step you can take today toward your biggest fear?",
        "perspective": "Courage is not the absence of fear; it is action in the presence of it. Do the thing, and you will get the power."
    },
    {
        "reflection": "Are you living your life, or performing it for an audience?",
        "perspective": "Social media has trained us to document moments rather than feel them. Put the phone down. The memory is worth more than the post."
    },
    {
        "reflection": "What feels like work to others, but feels like play to you?",
        "perspective": "That is your calling. Lean into it. Naval says: 'Specific knowledge is found by pursuing your genuine curiosity and passion rather than whatever is hot right now.'"
    },
    {
        "reflection": "What are you angry about?",
        "perspective": "Anger is often a punishment we give ourselves for someone else's mistake. Letting go is not forgiveness for them; it is freedom for you."
    },
    {
        "reflection": "If you lost everything you own today, who would you be?",
        "perspective": "You are not your job, your bank account, or your car. Strip it all away, and what remains is your character. Build that."
    },
    {
        "reflection": "Why are you rushing?",
        "perspective": "Nature does not hurry, yet everything is accomplished. Slow down. You cannot appreciate the view if you are only focused on the speedometer."
    },
    {
        "reflection": "What compliment do you struggle to accept?",
        "perspective": "The things we deny in ourselves are often our greatest strengths. Accept the kindness of others; they see a light in you that you might be missing."
    },
    {
        "reflection": "Is this problem going to matter in 5 years?",
        "perspective": "If the answer is no, do not spend more than 5 minutes being upset about it. Perspective is the antidote to stress."
    },
    {
        "reflection": "What does 'Success' actually look like to you, specifically?",
        "perspective": "If you don't define success for yourself, society will define it for you—and their definition usually involves you being tired and broke."
    },
    {
        "reflection": "What is the cost of your ambition?",
        "perspective": "Ambition is a vector; it has magnitude and direction. Ensure your ladder is leaning against the right wall before you climb to the top."
    },
    {
        "reflection": "When did you last sit in silence without a device?",
        "perspective": "Blaise Pascal said: 'All of humanity's problems stem from man's inability to sit quietly in a room alone.' Learn to be bored. It is where creativity is born."
    },
    {
        "reflection": "Who are you trying to impress?",
        "perspective": "The people you are trying to impress are likely too busy thinking about themselves to notice you. Be authentic. It attracts the right people."
    },
    {
        "reflection": "What is a bridge you need to burn?",
        "perspective": "Sometimes you have to burn bridges to stop yourself from crossing back to places you never belonged. Light the match."
    },
    {
        "reflection": "Are you a victim of your circumstances, or the architect of your response?",
        "perspective": "You cannot control the wind, but you can adjust the sails. Your power lies in your response, not the event."
    },
    {
        "reflection": "What did you love doing as a child that you stopped doing?",
        "perspective": "Go back there. That is where your pure joy lives. It wasn't about money or status then; it was about the soul."
    },
    {
        "reflection": "How do you treat people who can do nothing for you?",
        "perspective": "This is the truest test of character. Kindness is not a transaction; it is a state of being."
    },
    {
        "reflection": "What are you procrastinating on because you are afraid of doing it imperfectly?",
        "perspective": "Anything worth doing is worth doing poorly at first. Perfectionism is just procrastination in a fancy suit."
    },
    {
        "reflection": "Do you listen to understand, or do you listen to reply?",
        "perspective": "Most people never truly listen. Be the person who hears what isn't being said. That is a superpower."
    },
    {
        "reflection": "What is the story you keep telling yourself about why you 'can't'?",
        "perspective": "That story is a cage. You built it, and you have the key. Change the narrative, change the life."
    },
    {
        "reflection": "If you had 100 million dollars, but you were sick, would you trade it all for health?",
        "perspective": "Confucius said: 'A healthy man wants a thousand things, a sick man only wants one.' Do not sacrifice your health for wealth; it is a bad trade."
    },
    {
        "reflection": "Are you easier on others than you are on yourself?",
        "perspective": "Talk to yourself like you would to a friend. You deserve the same compassion you give away so freely."
    },
    {
        "reflection": "What are you tolerating?",
        "perspective": "You get what you tolerate. If you allow mediocrity, disrespect, or unhappiness, you will receive it in abundance. Raise your standards."
    },
    {
        "reflection": "Where are you seeking validation?",
        "perspective": "If you look for it outside, you will always be hungry. If you find it inside, you will always be full."
    },
    {
        "reflection": "What is the difference between giving up and knowing when to have had enough?",
        "perspective": "Giving up is driven by fear. Knowing when to stop is driven by self-respect. Know the difference."
    },
    {
        "reflection": "What habits do you have that are stealing your future?",
        "perspective": "First we make our habits, then our habits make us. Inspect your routine; it is the blueprint of your destiny."
    },
    {
        "reflection": "If everyone was blind, how many people would you impress?",
        "perspective": "Impress people with your soul, your mind, and your kindness. Those are the only things that can be seen in the dark."
    },
    {
        "reflection": "What is the most expensive thing you own that money didn't buy?",
        "perspective": "Your integrity. Your peace of mind. Your time. Protect these assets with your life."
    },
    {
        "reflection": "Are you avoiding pain, or pursuing growth?",
        "perspective": "Growth is painful. Change is painful. But nothing is as painful as staying stuck where you do not belong."
    },
    {
        "reflection": "What knowledge do you have that you are not applying?",
        "perspective": "To know and not to do is not to know. Wisdom is applied knowledge. Take action."
    },
    {
        "reflection": "What if the worst-case scenario happened? Could you handle it?",
        "perspective": "Usually, the answer is yes. You are stronger than you think. Once you accept the worst, you are free to pursue the best."
    },
    {
        "reflection": "Who are you when no one is watching?",
        "perspective": "That is the real you. Cultivate that person. Integrity is doing the right thing even when no one will ever know."
    },
    {
        "reflection": "What is a 'no' you need to say today?",
        "perspective": "A 'no' to others is often a 'yes' to yourself. Guard your time; it is the only non-renewable resource."
    },
    {
        "reflection": "Are you optimizing for resume virtues or eulogy virtues?",
        "perspective": "Resume virtues are skills for the marketplace. Eulogy virtues are the ones that get talked about at your funeral—whether you were kind, brave, honest. Focus on the latter."
    }
]

def generate_reflections_json():
    final_list = []
    current_date = START_DATE
    delta = timedelta(days=1)
    
    # We will shuffle the bank to ensure random order, 
    # but since we need 180+ days and have ~50 items, we will cycle through them.
    # To make it feel fresh, we shuffle a copy for each cycle.
    
    days_to_generate = (END_DATE - START_DATE).days + 1
    
    # Create a long list by repeating and shuffling
    long_list = []
    while len(long_list) < days_to_generate:
        chunk = reflection_bank[:] # Copy
        random.shuffle(chunk)      # Shuffle
        long_list.extend(chunk)    # Add to main list

    # Generate the JSON entries
    for i in range(days_to_generate):
        date_str = current_date.strftime("%d/%m/%Y")
        item = long_list[i]
        
        entry = {
            "date": date_str,
            "reflection": item["reflection"],
            "perspective": item["perspective"]
        }
        final_list.append(entry)
        current_date += delta

    # Write to file
    with open(OUTPUT_FILE, "w", encoding='utf-8') as f:
        json.dump(final_list, f, indent=4, ensure_ascii=False)
    
    print(f"Success! Generated {len(final_list)} daily reflections in '{OUTPUT_FILE}'")

if __name__ == "__main__":
    generate_reflections_json()