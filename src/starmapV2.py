import numpy as np
import sys
# Set up matplotlib
import matplotlib.pyplot as plt
from astropy.io import ascii

def build_map():
    data = ascii.read("lmxb_hmxb combined_cosmic sources.csv")
    import astropy.coordinates as coord
    import astropy.units as u
    new = []
    for i in range(len(data)):
        i_row = data[i] # get the first (ith) row
        ra = coord.Angle(i_row["RA"], unit=u.hour) # create an Angle object
        print(ra.degree) # convert to degrees
        new.append(ra.degree)
    ra = coord.Angle(new*u.degree)
    ra = ra.wrap_at(180*u.degree)
    import astropy.coordinates as coord
    import astropy.units as u
    new2 = []
    for i in range(len(data)):
        i_row = data[i] # get the first (ith) row
        dec = coord.Angle(i_row["Dec"], unit=u.deg)
        print(dec.degree) # convert to degrees
        new2.append(dec.degree)
    ra = coord.Angle(new*u.degree)
    ra = ra.wrap_at(180*u.degree)
    dec = coord.Angle(new2*u.degree)
    import matplotlib.pyplot as plt
    fig = plt.figure(figsize=(8,6))
    ax = fig.add_subplot(111, projection="mollweide")
    # ax.set_xticklabels(['14h','16h','18h','20h','22h','0h','2h','4h','6h','8h','10h'])
    sc = ax.scatter(ra.radian, dec.radian)
    annot = ax.annotate("", xy=(0,0), xytext=(20,20),textcoords="offset points",
                        bbox=dict(boxstyle="round", fc="w"),
                        arrowprops=dict(arrowstyle="->"))
    annot.set_visible(False)

    def update_annot(ind):

        pos = sc.get_offsets()[ind["ind"][0]]
        annot.xy = pos
        text = "{}, {}".format(" ".join(list(map(str,ind["ind"]))), 
                            " ".join([str(n) for n in ind["ind"]]))
        annot.set_text(text)
        annot.get_bbox_patch()
        # .set_facecolor(cmap(norm(c[ind["ind"][0]])))
        annot.get_bbox_patch().set_alpha(0.4)


    def hover(event):
        vis = annot.get_visible()
        if event.inaxes == ax:
            cont, ind = sc.contains(event)
            if cont:
                update_annot(ind)
                annot.set_visible(True)
                fig.canvas.draw_idle()
            else:
                if vis:
                    annot.set_visible(False)
                    fig.canvas.draw_idle()

    fig.canvas.mpl_connect("motion_notify_event", hover)

    ax.set_xticklabels(['14h','16h','18h','20h','22h','0h','2h','4h','6h','8h','10h'])
    ax.grid(True)
    plt.show()


# import mpld3
# N=280
# fig, ax = plt.subplots()
# t=ax.scatter(ra.radian, dec.radian)

# ax.set_xticklabels(['14h','16h','18h','20h','22h','0h','2h','4h','6h','8h','10h'])
# ax.grid(True)
# labels = ['point {0}'.format(i + 1) for i in range(N)]
# tooltip = mpld3.plugins.PointLabelTooltip(t, labels=labels)
# mpld3.plugins.connect(fig, tooltip)

# mpld3.display()
