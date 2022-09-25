
##include calc.h

double[][] countRed(double[][] u1, double[][] u0, double[] black, double[] red, double f, double a1, double an, double ai, int rnum)
{
    for (int i = 0; i < rnum; i++)
    {
        u1[red[i]] = -(a1 * (u0[red[i] - 1] + u0[red[i] + 1]) + an * (u0[red[i] + ny] + u0[red[i] - ny]) - f[red[i]]) / ai;
    }

    return u1
}

double[][] countBlack(double[][] u1, double[][] u0, double[] black, double[] red, double f, double a1, double an, double ai, int bnum)
{
    for (int i = 0; i < bnum; i++)
    {
        u1[black[i]] = -(a1 * (u1[black[i] - 1] + u1[black[i] + 1]) + an * (u1[black[i] + ny] + u1[black[i] - ny]) - f[black[i]]) / ai;
    }
    return u1;
}