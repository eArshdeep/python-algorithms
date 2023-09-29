# Merge Sort

| **Summary**       | |
| -                 | - |
| **Complexity**    | |
| Worst             | $O(nlog_{2}(n))$ |
| Best              | $\Omega(nlog_{2}(n))$ |
| Average           | $\Theta(nlog_{2}(n))$ |
| Space             | $O(n)$, $\Omega(n)$ |
| **Other**         | |
| Stable            | Yes |
| Recursion Depth   | $log_{2}(n)$ |

The good:

- Consistent complexity across best, worst, and average cases
- Stable (relative order of equivalent elements preserved)

The bad:

- Recursive overhead
- Additional space required, equal to the size of the additional input
