"""Command-line interface: ``bell-lab --shots 8192 --visibility 0.9``."""

import argparse

from bell.runner import run_chsh


def build_parser():
    p = argparse.ArgumentParser(
        prog="bell-lab",
        description="Simulate a CHSH Bell test and an illustrative entropy bound.",
    )
    p.add_argument("--shots", type=int, default=4096, help="shots per setting")
    p.add_argument("--visibility", type=float, default=1.0, help="noise visibility in [0, 1]")
    p.add_argument("--seed", type=int, default=None, help="simulator seed")
    p.add_argument("--product-state", action="store_true", help="use unentangled control")
    p.add_argument("--plot", action="store_true", help="show theory plots")
    return p


def main(argv=None):
    args = build_parser().parse_args(argv)
    res = run_chsh(args.shots, args.visibility, args.seed, args.product_state)

    print(f"Shots per setting : {res.shots}")
    print(f"Visibility        : {res.visibility:.3f}")
    print("Correlations      : " + ", ".join(f"{e:+.4f}" for e in res.model_correlations))
    print(f"CHSH S            : {res.s_value:.4f} +/- {res.std_error:.4f}")
    verdict = "violates" if res.s_value > 2.0 else "does not violate"
    print(f"Result {verdict} the classical bound S <= 2")
    print(f"Min-entropy bound : {res.entropy_bound:.4f} bits/round (illustrative)")

    if args.plot:
        from bell.plots import show_results

        show_results(args.visibility, measured_s=res.s_value)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
