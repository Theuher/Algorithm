public class MinimumSearchCost {
    static int sum(int[] freq, int i, int j) {
        int total = 0;
        for (int k = i; k <= j; k++) {
            total += freq[k];
        }
        return total;
    }

    public int optimalBST(int[] keys, int[] freq, int n) {
        int[][] cost = new int[n][n];
        for (int i = 0; i < n; i++) {
            cost[i][i] = freq[i];
        }
        for (int l = 2; l <= n; l++) {
            for (int i = 0; i <= n - l; i++) {
                int j = i + l - 1;
                cost[i][j] = Integer.MAX_VALUE;

                for (int r = i; r <= j; r++) {
                    int c = ((r > i) ? cost[i][r - 1] : 0) +
                            ((r < j) ? cost[r + 1][j] : 0) +
                            sum(freq, i, j);

                    if (c < cost[i][j]) {
                        cost[i][j] = c;
                    }
                }
            }
        }
        return cost[0][n - 1];
    }

    public static void main(String[] args) {
        int[] keys = { 5, 6 };
        int[] freq = { 17, 25 };
        int n = keys.length;

        MinimumSearchCost minimumSearchCost = new MinimumSearchCost();
        System.out
                .println("Minimum cost of Optimal Binary Search Tree: " + minimumSearchCost.optimalBST(keys, freq, n));
    }
}
