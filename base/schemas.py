from typing import List, Dict

from ninja import Router, Schema

router = Router(tags=["food"])


class QueryParamsSchema(Schema):
    def filters(self) -> Dict:
        _dict = self.dict(exclude_unset=True)
        return {k: v for k, v in _dict.items() if not k.startswith("by__")}

    def orders(self) -> List[str]:
        _dict = self.dict(exclude_unset=True)
        _dict = {k: v for k, v in _dict.items() if k.startswith("by__")}
        return [
            f"{'-' if order <= -1 else ''}{key.replace('by__', '')}"
            for key, order in sorted(_dict.items(), key=lambda x: abs(x[1]))
            if order != 0
        ]
