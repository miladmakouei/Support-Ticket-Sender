
import json
import urllib.request
import urllib.error


def send_ticket(customer_name, title, category, description):
    url = "https://jsonplaceholder.typicode.com/posts"

    ticket_data = {
        "customer_name": customer_name,
        "title": title,
        "category": category,
        "description": description
    }

    json_data = json.dumps(ticket_data).encode("utf-8")

    request = urllib.request.Request(
        url,
        data=json_data,
        headers={
            "Content-Type": "application/json"
        },
        method="POST"
    )

    try:
        with urllib.request.urlopen(request) as response:
            response_data = response.read().decode("utf-8")
            result = json.loads(response_data)

            return result

    except urllib.error.HTTPError as error:
        print(f"HTTP Error: {error.code}")

    except urllib.error.URLError:
        print("Connection error. Please check your internet.")

    except json.JSONDecodeError:
        print("Could not read the API response.")

    return None


def main():
    print("Support Ticket Sender")
    print("-" * 30)

    customer_name = input("Customer name: ").strip()
    title = input("Ticket title: ").strip()
    category = input("Ticket category: ").strip()
    description = input("Describe your problem: ").strip()

    if not customer_name or not title or not category or not description:
        print("\nAll fields are required.")
        return

    print("\nSending your support ticket...")

    result = send_ticket(
        customer_name,
        title,
        category,
        description
    )

    if result is not None:
        print("\nTicket submitted successfully!")
        print("-" * 30)
        print(f"Ticket ID: {result.get('id')}")
        print(f"Title: {result.get('title')}")
        print(f"Customer: {result.get('customer_name')}")
        print(f"Category: {result.get('category')}")


if __name__ == "__main__":
    main()
