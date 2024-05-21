# Wikipedia
---
```#bash
$pkg install python
$pkg install python2
$pkg install git
$git clone https://github.com/Ro706/Wikipedia-.git
$cd Wikipedia 
$chmod +X *
$python3 1.py
```
---

# Wikipedia Summary Program

This Python script allows you to retrieve a summary of a Wikipedia article based on user input. It uses the `wikipedia` library to fetch the summary.

## Usage

1. Make sure you have Python installed on your system.
2. Install the `wikipedia-api` library using `pip install wikipedia-api`.
3. Run the script (`1.py`) in your terminal or IDE.
4. Enter the topic you want to learn about when prompted.
5. The script will fetch the Wikipedia summary for that topic and display it.

## Features

- Provides a concise summary of Wikipedia articles.
- Handles disambiguation errors by suggesting specific topics.
- Alerts the user if the topic does not exist or if there's an HTTP timeout.

## Dependencies

- Python 3.x
- `wikipedia-api` library

## Example

```python
import wikipedia

def main():
    print("Welcome to the Wikipedia Summary Program!")
    while True:
        topic = input("Enter a topic to get a summary (or 'q' to quit): ")
        if topic.lower() == 'q':
            print("Thank you for using the Wikipedia Summary Program!")
            break
        try:
            summary = wikipedia.summary(topic)
            print("\nSummary for '{}':\n{}".format(topic, summary))
        except wikipedia.exceptions.DisambiguationError as e:
            print("\nDisambiguation Error: Please provide a more specific topic.")
            print("Options: {}\n".format(", ".join(e.options)))
        except wikipedia.exceptions.PageError:
            print("\nPage Error: The topic '{}' does not exist on Wikipedia.\n".format(topic))
        except wikipedia.exceptions.HTTPTimeoutError:
            print("\nHTTP Timeout Error: Unable to connect to Wikipedia. Please try again later.\n")
        except Exception as e:
            print("\nAn error occurred: {}\n".format(e))

if __name__ == "__main__":
    main()
```

