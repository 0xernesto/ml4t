import matplotlib.dates as mdates


def plot_data(df_data, title, ylabel):
    """Plot asset data with appropriate axis labels."""
    axis = df_data.plot(title=title, fontsize=12)
    axis.set_xlabel("Date")
    axis.set_ylabel(ylabel)

    # Format the x-axis to show month abbreviations
    axis.xaxis.set_major_formatter(mdates.DateFormatter("%b %Y"))
