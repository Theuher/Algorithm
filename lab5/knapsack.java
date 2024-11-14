public class knapsack {
    public int knapsacksol(int[] weights, int[] values, int capacity) {
        int n = values.length;
        int[][] dp = new int[n + 1][capacity + 1];

        for (int i = 1; i <= n; i++) {
            for (int w = 1; w <= capacity; w++) {
                if (weights[i - 1] <= w) {
                    dp[i][w] = Math.max(dp[i - 1][w], dp[i - 1][w - weights[i - 1]] + values[i - 1]);
                } else {
                    dp[i][w] = dp[i - 1][w];
                }
            }
        }

        return dp[n][capacity];
    }

    public static void main(String[] args) {
        knapsack kna = new knapsack();
        int a[] = new int[5];
        int v[] = new int[5];
        for (int i = 0; i < 5; i++) {
            a[i] = (i + 1) * 100;
        }
        v[0] = 50;// 100
        v[1] = 120;// 200
        v[2] = 230;// 300
        v[3] = 330;// 400
        v[4] = 240;// 500

        System.out.println(kna.knapsacksol(a, v, 1000));
    }
}