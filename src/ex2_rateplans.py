import json
from dataclasses import dataclass
from typing import Generator, List


FILE_PATH = "rateplans.json"


@dataclass
class RatePlan:
    name: str
    tags: List[str]


class RatePlansSearcher:
    """
    Loads rateplan data and provides methods to allow it to be searched
    """

    def __init__(self) -> None:
        self.rateplans = self._load_json_rateplans()

    def _load_json_rateplans(self) -> List[RatePlan]:
        """
        Load RatePlan objects from a json file.
        """
        with open(FILE_PATH) as stream:
            return [
                RatePlan(name=rp["name"], tags=rp["tags"])
                for rp in json.load(stream)["rateplans"]
            ]

    def search(self, tag: str) -> Generator[RatePlan, None, None]:
        """
        Generator that yields all rateplans in self.rateplans with a matching tag.
        """
        for rateplan in self.rateplans:
            for candidate_tag in rateplan.tags:
                if candidate_tag == tag:
                    yield rateplan


# ---------------------------------------------------------------
# Example run
# ---------------------------------------------------------------
def main() -> None:
    searcher = RatePlansSearcher()
    for rateplan in searcher.search("deluxe"):
        print(rateplan)
    print("OK")


if __name__ == "__main__":
    main()
