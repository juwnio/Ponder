# Ponder

Ponder is a proof of concept script originally created to explore communication between multiple APIs. It later evolved into a fun and responsive tool for generating and posting content.

## How It Works

1. **API Integration:**
   - Ponder uses the Groq API to generate creative content based on a given context, style, and story objects.
   - It then posts the generated content to Twitter using the Tweepy library.

2. **Configuration:**
   - All API keys and tokens are stored in a `.env` file. See `.env.example` for the required variables.
   - The program loads these credentials automatically at runtime.

3. **Running the Program:**
   - Install dependencies: `pip install -r requirements.txt`
   - Create a `.env` file with your API credentials.
   - Run the main script (e.g., `python ponder/ponder.py`).

## Future Improvements, Maybe

*`I do not plan on updating this repository as often because of prioritery needs of attention from other projects, but if i ever do:`*

- I wider range of philosophers & Topics (less ambiguous), external iteration option of these names and topics.





<a href="https://groq.com" target="_blank" rel="noopener noreferrer">
  <img
    src="https://console.groq.com/powered-by-groq.svg"
    alt="Powered by Groq for fast inference."
  />
</a>
