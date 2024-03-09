import random

# Define the Tarot cards
tarot_cards = {
    'The Fool': '🤡', 'The Magician': '🧙‍♂️', 'The High Priestess': '🔮',
    'The Empress': '👸', 'The Emperor': '👑', 'The Hierophant': '📜',
    'The Lovers': '💑', 'The Chariot': '🏎️', 'Strength': '💪',
    'The Hermit': '🕯️', 'Wheel of Fortune': '🎡', 'Justice': '⚖️',
    'The Hanged Man': '👻', 'Death': '💀', 'Temperance': '🌡️',
    'The Devil': '😈', 'The Tower': '🏰', 'The Star': '⭐',
    'The Moon': '🌙', 'The Sun': '☀️', 'Judgement': '👼',
    'The World': '🌍'
}

# Define the regular playing cards with new emojis
playing_cards = {
    'Ace🂡': '🂡', 'Two🂢': '🂢', 'Three🂣': '🂣', 'Four🂤': '🂤', 'Five🂥': '🂥',
    'Six🂦': '🂦', 'Seven🂧': '🂧', 'Eight🂨': '🂨', 'Nine🂩': '🂩', 'Ten🂪': '🂪',
    'Page🃏': '🃏', 'Knight♞': '♞', 'Queen♚': '♚', 'King♛': '♛',   
}
# Define meanings for the minor arcana cards
minor_arcana_meanings = {
    
    'Ace🂡 of ☕Cups': 'Emotional Beginnings, Love, Intuition',
    'Two🂢 of ☕Cups': 'Partnership, Union, Connection',
    'Three🂣 of ☕Cups': 'Celebration, Friendship, Joy',
    'Four🂤 of ☕Cups': 'Contemplation, Rest, Meditation',
    'Five🂥 of ☕Cups': 'Loss, Grief, Moving On',
    'Six🂦 of ☕Cups': 'Nostalgia, Reunion, Childhood',
    'Seven🂧 of ☕Cups': 'Choices, Fantasy, Imagination',
    'Eight🂨 of ☕Cups': 'Soul-Searching, Abandonment, Transition',
    'Nine🂩 of ☕Cups': 'Contentment, Satisfaction, Wishes',
    'Ten🂪 of ☕Cups': 'Harmony, Family, Fulfillment',
    'Page🃏 of ☕Cups': 'Dreamy Exploration, Creativity, Intuition',
    'Knight♞ of ☕Cups': 'Romantic Pursuit, Love, Adventure',
    'Queen♚ of ☕Cups': 'Nurturing Emotions, Compassion, Empathy',
    'King♛ of ☕Cups': 'Emotional Mastery, Wisdom, Leadership',
    'Ace🂡 of ⚔️Swords': 'Clarity, Truth, Mental Power',
    'Two🂢 of ⚔️Swords': 'Decision, Stalemate, Balance',
    'Three🂣 of ⚔️Swords': 'Heartbreak, Suffering, Release',
    'Four🂤 of ⚔️Swords': 'Rest, Contemplation, Rejuvenation',
    'Five🂥 of ⚔️Swords': 'Conflict, Defeat, Hostility',
    'Six🂦 of ⚔️Swords': 'Transition, Moving On, Calm',
    'Seven🂧 of ⚔️Swords': 'Deception, Stealth, Strategy',
    'Eight🂨 of ⚔️Swords': 'Restriction, Imprisonment, Self-Boundaries',
    'Nine🂩 of ⚔️Swords': 'Anxiety, Nightmares, Guilt',
    'Ten🂪 of ⚔️Swords': 'Endings, Rock Bottom, Transformation',
    'Page🃏 of ⚔️Swords': 'Curiosity, Investigation, New Ideas',
    'Knight♞ of ⚔️Swords': 'Ambition, Action, Assertiveness',
    'Queen♚ of ⚔️Swords': 'Independence, Logic, Wit',
    'King♛ of ⚔️Swords': 'Authority, Clarity, Intellectual Power',
    'Ace🂡 of 💰Pentacles': 'Manifestation, Abundance, New Beginnings',
    'Two🂢 of 💰Pentacles': 'Balance, Adaptability, Juggling',
    'Three🂣 of 💰Pentacles': 'Teamwork, Collaboration, Mastery',
    'Four🂤 of 💰Pentacles': 'Stability, Security, Possessiveness',
    'Five🂥 of 💰Pentacles': 'Hardship, Poverty, Endurance',
    'Six🂦 of 💰Pentacles': 'Generosity, Charity, Prosperity',
    'Seven🂧 of 💰Pentacles': 'Patience, Investment, Harvest',
    'Eight🂨 of 💰Pentacles': 'Dedication, Skill, Craftsmanship',
    'Nine🂩 of 💰Pentacles': 'Self-Sufficiency, Luxury, Independence',
    'Ten🂪 of 💰Pentacles': 'Legacy, Wealth, Family',
    'Page🃏 of 💰Pentacles': 'Learning, Study, Practicality',
    'Knight♞ of 💰Pentacles': 'Responsibility, Reliability, Hard Work',
    'Queen♚ of 💰Pentacles': 'Nurturing, Practicality, Homeliness',
    'King♛ of 💰Pentacles': 'Abundance, Success, Financial Stability',
    'Ace🂡 of ☄️Wands': 'Inspiration, Creation, New Beginnings',
    'Two🂢 of ☄️Wands': 'Planning, Progress, Exploration',
    'Three🂣 of ☄️Wands': 'Expansion, Leadership, Foresight',
    'Four🂤 of ☄️Wands': 'Celebration, Harmony, Achievements',
    'Five🂥 of ☄️Wands': 'Competition, Conflict, Challenges',
    'Six🂦 of ☄️Wands': 'Victory, Recognition, Success',
    'Seven🂧 of ☄️Wands': 'Defense, Courage, Perseverance',
    'Eight🂨 of ☄️Wands': 'Swiftness, Progress, Communication',
    'Nine🂩 of ☄️Wands': 'Resilience, Stamina, Persistence',
    'Ten🂪 of ☄️Wands': 'Burden, Overwhelm, Responsibility',
    'Page🃏 of ☄️Wands': 'Enthusiasm, Exploration, Discovery',
    'Knight♞ of ☄️Wands': 'Action, Adventure, Spontaneity',
    'Queen♚ of ☄️Wands': 'Confidence, Passion, Leadership',
    'King♛ of ☄️Wands': 'Authority, Inspiration, Charisma'
}

suits = ['☕Cups', '⚔️Swords', '💰Pentacles', '☄️Wands']

def shuffle_cards():
    # Combine and shuffle the Tarot and regular playing cards
    all_cards = list(tarot_cards.keys()) + [f'{rank} of {suit}' for rank in playing_cards.keys() for suit in suits]
    random.shuffle(all_cards)
    return all_cards

def draw_cards(cards, num_cards):
    drawn_cards = random.sample(cards, num_cards)
    for card in drawn_cards:
        cards.remove(card)
    return drawn_cards

def draw_past_present_future(num_cards):
    all_cards = shuffle_cards()
    past = draw_cards(all_cards, num_cards)
    present = draw_cards(all_cards, num_cards)
    future = draw_cards(all_cards, num_cards)
    return past, present, future

def draw_now(num_cards):
    all_cards = shuffle_cards()
    now = draw_cards(all_cards, num_cards)
    return now

def display_cards(cards, emoji_before_number=False):
    for card in cards:
        card_name = card.split(' of ')[-1].strip()
        emoji = tarot_cards.get(card_name, playing_cards.get(card_name, ''))
        number = card.split(' ')[0]
        suit = card.split(' of ')[-1]
        if emoji_before_number:
            print(f"  {number} {emoji} of {suit} - {minor_arcana_meanings.get(card, 'No meaning available')}")
        else:
            print(f"  {number} {emoji} {card_name} - {minor_arcana_meanings.get(card, 'No meaning available')}")

def main():
    print("Welcome to the Tarot Card Game!")

    while True:
        print("\nChoose a type of drawing:")
        print("1. 3 Simple (1 card draw three times)")
        print("2. 6 Medium (2 card draw three times)")
        print("3. 9 Expert (3 cards drawn three times)")
        print("4. 1 Fast (1 card draw)")
        print("Type 'exit' to end.")
        
        choice = input("Enter the number of your choice: ")

        if choice == 'exit':
            break
        elif choice == '1':
            num_cards = 1
            draws = 3
        elif choice == '2':
            num_cards = 2
            draws = 3
        elif choice == '3':
            num_cards = 3
            draws = 3
        elif choice == '4':
            num_cards = 1
            draws = 1
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")
            continue

        for _ in range(draws):
            if choice == '4':
                now = draw_now(num_cards)
                print("\nNow:")
                display_cards(now, emoji_before_number=True)
            else:
                past, present, future = draw_past_present_future(num_cards)
                print("\nPast:")
                display_cards(past, emoji_before_number=True)
                input("Press Enter to draw the Present cards...")
                print("\nPresent:")
                display_cards(present, emoji_before_number=True)
                input("Press Enter to draw the Future cards...")
                print("\nFuture:")
                display_cards(future, emoji_before_number=True)

if __name__ == "__main__":
    main()


























































import random

# Define the Tarot cards
tarot_cards = {
    'The Fool': '🤡', 'The Magician': '🧙‍♂️', 'The High Priestess': '🔮',
    'The Empress': '👸', 'The Emperor': '👑', 'The Hierophant': '📜',
    'The Lovers': '💑', 'The Chariot': '🏎️', 'Strength': '💪',
    'The Hermit': '🕯️', 'Wheel of Fortune': '🎡', 'Justice': '⚖️',
    'The Hanged Man': '👻', 'Death': '💀', 'Temperance': '🌡️',
    'The Devil': '😈', 'The Tower': '🏰', 'The Star': '⭐',
    'The Moon': '🌙', 'The Sun': '☀️', 'Judgement': '👼',
    'The World': '🌍'
}

# Define the regular playing cards with new emojis
playing_cards = {
    'Ace🂡': '🂡', 'Two🂢': '🂢', 'Three🂣': '🂣', 'Four🂤': '🂤', 'Five🂥': '🂥',
    'Six🂦': '🂦', 'Seven🂧': '🂧', 'Eight🂨': '🂨', 'Nine🂩': '🂩', 'Ten🂪': '🂪',
    'Page🃏': '🃏', 'Knight♞': '♞', 'Queen♚': '♚', 'King♛': '♛',   
}
# Define meanings for the minor arcana cards
minor_arcana_meanings = {
    'Ace🂡 of ☕Cups': 'Emotional Beginnings, Love, Intuition',
    'Two🂢 of ☕Cups': 'Partnership, Union, Connection',
    'Three🂣 of ☕Cups': 'Celebration, Friendship, Joy',
    'Four🂤 of ☕Cups': 'Contemplation, Rest, Meditation',
    'Five🂥 of ☕Cups': 'Loss, Grief, Moving On',
    'Six🂦 of ☕Cups': 'Nostalgia, Reunion, Childhood',
    'Seven🂧 of ☕Cups': 'Choices, Fantasy, Imagination',
    'Eight🂨 of ☕Cups': 'Soul-Searching, Abandonment, Transition',
    'Nine🂩 of ☕Cups': 'Contentment, Satisfaction, Wishes',
    'Ten🂪 of ☕Cups': 'Harmony, Family, Fulfillment',
    'Page🃏 of ☕Cups': 'Dreamy Exploration, Creativity, Intuition',
    'Knight♞ of ☕Cups': 'Romantic Pursuit, Love, Adventure',
    'Queen♚ of ☕Cups': 'Nurturing Emotions, Compassion, Empathy',
    'King♛ of ☕Cups': 'Emotional Mastery, Wisdom, Leadership',
    'Ace🂡 of ⚔️Swords': 'Clarity, Truth, Mental Power',
    'Two🂢 of ⚔️Swords': 'Decision, Stalemate, Balance',
    'Three🂣 of ⚔️Swords': 'Heartbreak, Suffering, Release',
    'Four🂤 of ⚔️Swords': 'Rest, Contemplation, Rejuvenation',
    'Five🂥 of ⚔️Swords': 'Conflict, Defeat, Hostility',
    'Six🂦 of ⚔️Swords': 'Transition, Moving On, Calm',
    'Seven🂧 of ⚔️Swords': 'Deception, Stealth, Strategy',
    'Eight🂨 of ⚔️Swords': 'Restriction, Imprisonment, Self-Boundaries',
    'Nine🂩 of ⚔️Swords': 'Anxiety, Nightmares, Guilt',
    'Ten🂪 of ⚔️Swords': 'Endings, Rock Bottom, Transformation',
    'Page🃏 of ⚔️Swords': 'Curiosity, Investigation, New Ideas',
    'Knight♞ of ⚔️Swords': 'Ambition, Action, Assertiveness',
    'Queen♚ of ⚔️Swords': 'Independence, Logic, Wit',
    'King♛ of ⚔️Swords': 'Authority, Clarity, Intellectual Power',
    'Ace🂡 of 💰Pentacles': 'Manifestation, Abundance, New Beginnings',
    'Two🂢 of 💰Pentacles': 'Balance, Adaptability, Juggling',
    'Three🂣 of 💰Pentacles': 'Teamwork, Collaboration, Mastery',
    'Four🂤 of 💰Pentacles': 'Stability, Security, Possessiveness',
    'Five🂥 of 💰Pentacles': 'Hardship, Poverty, Endurance',
    'Six🂦 of 💰Pentacles': 'Generosity, Charity, Prosperity',
    'Seven🂧 of 💰Pentacles': 'Patience, Investment, Harvest',
    'Eight🂨 of 💰Pentacles': 'Dedication, Skill, Craftsmanship',
    'Nine🂩 of 💰Pentacles': 'Self-Sufficiency, Luxury, Independence',
    'Ten🂪 of 💰Pentacles': 'Legacy, Wealth, Family',
    'Page🃏 of 💰Pentacles': 'Learning, Study, Practicality',
    'Knight♞ of 💰Pentacles': 'Responsibility, Reliability, Hard Work',
    'Queen♚ of 💰Pentacles': 'Nurturing, Practicality, Homeliness',
    'King♛ of 💰Pentacles': 'Abundance, Success, Financial Stability',
    'Ace🂡 of ☄️Wands': 'Inspiration, Creation, New Beginnings',
    'Two🂢 of ☄️Wands': 'Planning, Progress, Exploration',
    'Three🂣 of ☄️Wands': 'Expansion, Leadership, Foresight',
    'Four🂤 of ☄️Wands': 'Celebration, Harmony, Achievements',
    'Five🂥 of ☄️Wands': 'Competition, Conflict, Challenges',
    'Six🂦 of ☄️Wands': 'Victory, Recognition, Success',
    'Seven🂧 of ☄️Wands': 'Defense, Courage, Perseverance',
    'Eight🂨 of ☄️Wands': 'Swiftness, Progress, Communication',
    'Nine🂩 of ☄️Wands': 'Resilience, Stamina, Persistence',
    'Ten🂪 of ☄️Wands': 'Burden, Overwhelm, Responsibility',
    'Page🃏 of ☄️Wands': 'Enthusiasm, Exploration, Discovery',
    'Knight♞ of ☄️Wands': 'Action, Adventure, Spontaneity',
    'Queen♚ of ☄️Wands': 'Confidence, Passion, Leadership',
    'King♛ of ☄️Wands': 'Authority, Inspiration, Charisma',
}

# Define meanings for the major arcana cards
major_arcana_meanings = {
    'The Fool': 'Spontaneity, Innocence, Beginnings',
    'The Magician': 'Manifestation, Power, Will',
    'The High Priestess': 'Intuition, Mystery, Feminine',
    'The Empress': 'Nurturing, Abundance, Fertility',
    'The Emperor': 'Authority, Structure, Leadership',
    'The Hierophant': 'Tradition, Spirituality, Guidance',
    'The Lovers': 'Connection, Harmony, Choice',
    'The Chariot': 'Determination, Control, Victory',
    'Strength': 'Courage, Inner Power, Patience',
    'The Hermit': 'Solitude, Reflection, Wisdom',
    'Wheel of Fortune': 'Change, Destiny, Cycles',
    'Justice': 'Fairness, Truth, Balance',
    'The Hanged Man': 'Surrender, Release, Perspective',
    'Death': 'Transformation, Endings, Rebirth',
    'Temperance': 'Harmony, Moderation, Healing',
    'The Devil': 'Temptation, Bondage, Materialism',
    'The Tower': 'Upheaval, Chaos, Revelation',
    'The Star': 'Hope, Inspiration, Spirituality',
    'The Moon': 'Illusion, Intuition, Dreams',
    'The Sun': 'Vitality, Joy, Success',
    'The Judgement': 'Rebirth, Redemption, Awakening',
    'The World': 'Completion, Fulfillment, Wholeness'
}

suits = ['☕Cups', '⚔️Swords', '💰Pentacles', '☄️Wands']

def shuffle_cards():
    # Combine and shuffle the Tarot and regular playing cards
    all_cards = list(tarot_cards.keys()) + [f'{rank} of {suit}' for rank in playing_cards.keys() for suit in suits]
    random.shuffle(all_cards)
    return all_cards

def draw_cards(cards, num_cards):
    drawn_cards = random.sample(cards, num_cards)
    for card in drawn_cards:
        cards.remove(card)
    return drawn_cards

def draw_past_present_future(num_cards):
    all_cards = shuffle_cards()
    past = draw_cards(all_cards, num_cards)
    present = draw_cards(all_cards, num_cards)
    future = draw_cards(all_cards, num_cards)
    return past, present, future

def draw_now(num_cards):
    all_cards = shuffle_cards()
    now = draw_cards(all_cards, num_cards)
    return now

def display_cards(cards, emoji_before_number=False):
    for card in cards:
        card_name = card.split(' of ')[-1].strip()
        emoji = tarot_cards.get(card_name, playing_cards.get(card_name, ''))
        number = card.split(' ')[0]
        suit = card.split(' of ')[-1]
        if emoji_before_number:
            print(f"  {number} {emoji} of {suit} - {minor_arcana_meanings.get(card, major_arcana_meanings.get(card, 'No meaning available'))}")
        else:
            print(f"  {number} {emoji} {card_name} - {minor_arcana_meanings.get(card, major_arcana_meanings.get(card, 'No meaning available'))}")

def main():
    print("Welcome to the Tarot Card Game!")

    while True:
        print("\nChoose a type of drawing:")
        print("1. 3 Simple (1 card draw three times)")
        print("2. 6 Medium (2 card draw three times)")
        print("3. 9 Expert (3 cards drawn three times)")
        print("4. 1 Fast (1 card draw)")
        print("Type 'exit' to end.")
        
        choice = input("Enter the number of your choice: ")

        if choice == 'exit':
            break
        elif choice == '1':
            num_cards = 1
            draws = 3
        elif choice == '2':
            num_cards = 2
            draws = 3
        elif choice == '3':
            num_cards = 3
            draws = 3
        elif choice == '4':
            num_cards = 1
            draws = 1
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")
            continue

        for _ in range(draws):
            if choice == '4':
                now = draw_now(num_cards)
                print("\nNow:")
                display_cards(now, emoji_before_number=True)
            else:
                past, present, future = draw_past_present_future(num_cards)
                print("\nPast:")
                display_cards(past, emoji_before_number=True)
                input("Press Enter to draw the Present cards...")
                print("\nPresent:")
                display_cards(present, emoji_before_number=True)
                input("Press Enter to draw the Future cards...")
                print("\nFuture:")
                display_cards(future, emoji_before_number=True)

if __name__ == "__main__":
    main()
