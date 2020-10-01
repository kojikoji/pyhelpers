def make_disc(vec, res):
    disc_vec = (pd.Series(vec).rank(pct=True) * res).astype(int)
    disc_vec[disc_vec == res] = res - 1
    return(disc_vec)
