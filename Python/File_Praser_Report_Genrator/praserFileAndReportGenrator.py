import csv
import json
import os


# 1. FILE PARSER

class FileParser:
    """
    Reads CSV and JSON files and converts them
    into a list of dictionaries.
    """

    def __init__(self, filename):
        self.filename = filename
        self.data = []

    def parse(self):
        """
        Detect the file type and parse it.
        """

        extension = os.path.splitext(self.filename)[1].lower()

        if extension == ".csv":
            self.data = self.parse_csv()

        elif extension == ".json":
            self.data = self.parse_json()

        else:
            raise ValueError(
                "Unsupported file format. "
                "Please use CSV or JSON."
            )

        return self.data

    # CSV parser

    def parse_csv(self):
        """
        Read CSV file and return a list of dictionaries.
        """

        try:
            with open(
                self.filename,
                "r",
                encoding="utf-8"
            ) as file:

                reader = csv.DictReader(file)

                data = []

                for row in reader:

                    # Clean column names
                    cleaned_row = {}

                    for key, value in row.items():

                        # Ignore empty column names
                        if key is None or key.strip() == "":
                            continue

                        clean_key = key.strip()

                        # Remove extra spaces from values
                        if isinstance(value, str):
                            value = value.strip()

                        cleaned_row[clean_key] = value

                    data.append(cleaned_row)

                return data

        except FileNotFoundError:
            raise FileNotFoundError(
                f"File not found: {self.filename}"
            )

        except PermissionError:
            raise PermissionError(
                f"Permission denied: {self.filename}"
            )

    # JSON parser
    
    def parse_json(self):
        """
        Read JSON file and return a list of dictionaries.
        """

        try:
            with open(
                self.filename,
                "r",
                encoding="utf-8"
            ) as file:

                data = json.load(file)

            # JSON should normally contain a list
            if isinstance(data, list):
                return data

            # If JSON contains {"data": [...]}
            if isinstance(data, dict):

                if "data" in data:
                    return data["data"]

                if "records" in data:
                    return data["records"]

            raise ValueError(
                "JSON must contain a list of records."
            )

        except FileNotFoundError:
            raise FileNotFoundError(
                f"File not found: {self.filename}"
            )

        except json.JSONDecodeError:
            raise ValueError(
                "The JSON file contains invalid JSON."
            )


# 2. REPORT GENERATOR

class ReportGenerator:
    """
    Analyzes cybersecurity attack data
    and generates a report.
    """

    def __init__(self, data):
        self.data = data

    # Total number of attacks

    def total_attacks(self):
        return len(self.data)

    # Count values in a specific column

    def count_by_field(self, field):
        """
        Count how many times each value appears
        in a particular field.
        """

        counts = {}

        for row in self.data:

            value = row.get(field, "")

            if value == "":
                value = "Unknown"

            if value not in counts:
                counts[value] = 0

            counts[value] += 1

        return counts

    # Sort dictionary by count

    def sort_counts(self, counts):
        """
        Sort values from highest count to lowest count.
        """

        return sorted(
            counts.items(),
            key=lambda item: item[1],
            reverse=True
        )

    # Most common value

    def most_common(self, field):
        """
        Find the most common value in a field.
        """

        counts = self.count_by_field(field)

        if not counts:
            return "No data"

        sorted_counts = self.sort_counts(counts)

        return sorted_counts[0]

    # Top N values

    def top_values(self, field, number=10):
        """
        Return the top N most common values.
        """

        counts = self.count_by_field(field)

        sorted_counts = self.sort_counts(counts)

        return sorted_counts[:number]

    # Find attacks containing a keyword

    def search_attacks(self, keyword):
        """
        Find attacks where the keyword appears
        in the title or attack type.
        """

        keyword = keyword.lower()

        results = [
            row
            for row in self.data
            if keyword in row.get("Title", "").lower()
            or keyword in row.get("Attack Type", "").lower()
        ]

        return results

    # Count attacks containing a keyword

    def count_keyword(self, keyword):
        return len(self.search_attacks(keyword))

    # Generator example

    def attack_titles(self):
        """
        Generator that produces attack titles one at a time.
        """

        for row in self.data:
            yield row.get("Title", "Unknown")

    # Generate report

    def generate_report(self):
        """
        Create the complete report as a string.
        """

        total = self.total_attacks()

        attack_types = self.top_values(
            "Attack Type",
            10
        )

        categories = self.top_values(
            "Category",
            10
        )

        targets = self.top_values(
            "Target Type",
            10
        )

        mitre = self.top_values(
            "MITRE Technique",
            10
        )

        impacts = self.top_values(
            "Impact",
            10
        )

        detection_methods = self.top_values(
            "Detection Method",
            10
        )

        # Build report
        report = []

        report.append("=" * 70)
        report.append("CYBERSECURITY ATTACK DATASET REPORT")
        report.append("=" * 70)

        report.append("")
        report.append(f"Total attacks: {total}")

        # Attack Types

        report.append("")
        report.append("-" * 70)
        report.append("TOP ATTACK TYPES")
        report.append("-" * 70)

        for value, count in attack_types:
            report.append(
                f"{value}: {count}"
            )

        # Categories

        report.append("")
        report.append("-" * 70)
        report.append("TOP CATEGORIES")
        report.append("-" * 70)

        for value, count in categories:
            report.append(
                f"{value}: {count}"
            )

        # Target Types

        report.append("")
        report.append("-" * 70)
        report.append("TOP TARGET TYPES")
        report.append("-" * 70)

        for value, count in targets:
            report.append(
                f"{value}: {count}"
            )

        # MITRE Techniques

        report.append("")
        report.append("-" * 70)
        report.append("TOP MITRE TECHNIQUES")
        report.append("-" * 70)

        for value, count in mitre:
            report.append(
                f"{value}: {count}"
            )

        # Impacts

        report.append("")
        report.append("-" * 70)
        report.append("TOP IMPACTS")
        report.append("-" * 70)

        for value, count in impacts:
            report.append(
                f"{value}: {count}"
            )

        # Detection Methods

        report.append("")
        report.append("-" * 70)
        report.append("TOP DETECTION METHODS")
        report.append("-" * 70)

        for value, count in detection_methods:
            report.append(
                f"{value}: {count}"
            )

        # Keyword analysis

        report.append("")
        report.append("-" * 70)
        report.append("COMMON ATTACK KEYWORDS")
        report.append("-" * 70)

        keywords = [
            "SQL",
            "Phishing",
            "Malware",
            "Ransomware",
            "DDoS",
            "XSS"
        ]

        for keyword in keywords:

            count = self.count_keyword(keyword)

            report.append(
                f"{keyword}: {count}"
            )

        report.append("")
        report.append("=" * 70)
        report.append("END OF REPORT")
        report.append("=" * 70)

        return "\n".join(report)


# 3. SAVE REPORT TO FILE

def save_report(report, filename="cybersecurity_report.txt"):
    """
    Save generated report to a text file.
    """

    try:
        with open(
            filename,
            "w",
            encoding="utf-8"
        ) as file:

            file.write(report)

        print(
            f"\nReport saved successfully to: {filename}"
        )

    except PermissionError:
        print(
            "Error: Permission denied while saving report."
        )


# 4. MAIN PROGRAM

def main():

    print("FILE PARSER and Report Genrator")

    filename = input(
        "\nEnter CSV/JSON filename: "
    ).strip()

    try:

        # Parse file

        parser = FileParser(filename)

        data = parser.parse()

        # Check if data exists

        if not data:

            print(
                "\nThe file contains no records."
            )

            return

        print(
            f"\nSuccessfully loaded {len(data)} records."
        )

        # Generate report

        report_generator = ReportGenerator(data)

        report = report_generator.generate_report()

        # Display report
        
        print("\n")
        print(report)

        # Save report

        save_report(report)

    except FileNotFoundError as error:

        print(
            f"\nERROR: {error}"
        )

    except ValueError as error:

        print(
            f"\nERROR: {error}"
        )

    except PermissionError as error:

        print(
            f"\nERROR: {error}"
        )

    except Exception as error:

        print(
            f"\nUnexpected error: {error}"
        )

# 5. PROGRAM ENTRY POINT

if __name__ == "__main__":
    main()