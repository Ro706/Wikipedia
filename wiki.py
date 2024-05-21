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
