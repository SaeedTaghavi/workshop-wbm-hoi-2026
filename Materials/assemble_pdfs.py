#!/usr/bin/env python3
"""Reconstruct workshop PDF slide decks from binary parts in this repository."""
from hashlib import sha256
from pathlib import Path
from shutil import copyfileobj

BASE = Path(__file__).resolve().parent
PDFS = {
    "Rodrigo_Cofre/RCofre_Whole_Brain_Models.pdf": (3, "f2f4e5a70017e92f84fa74525f1bb2bed136f799b54f2d1ff9628080c55388c3"),
    "Yonatan_Sanz_Perl/YSanz_Physics_of_Cognition.pdf": (4, "37f959806b8f7994d2ac4321418acdc0ff4c9a30d58354c94e16467b3dfa0b54"),
    "Xiaoge_Bao/Xiaoge_Pre.pdf": (2, "576a52d16dbbd42f6b7522a59b5d89c714b97da6bf312717ba2309ee7db6a952"),
}

def main():
    for rel, (count, expected) in PDFS.items():
        output = BASE / rel
        parts = [output.with_name(f"{output.name}.part{i:03d}") for i in range(1, count + 1)]
        missing = [str(p) for p in parts if not p.is_file()]
        if missing:
            raise FileNotFoundError(f"Missing parts for {output.name}: {missing}")
        temp = output.with_name(output.name + ".tmp")
        try:
            with temp.open("wb") as dest:
                for part in parts:
                    with part.open("rb") as src:
                        copyfileobj(src, dest)
            if sha256(temp.read_bytes()).hexdigest() != expected:
                raise ValueError(f"SHA-256 mismatch for {rel}")
            temp.replace(output)
            print(f"Verified: {output.relative_to(BASE)}")
        finally:
            temp.unlink(missing_ok=True)

if __name__ == "__main__":
    main()
