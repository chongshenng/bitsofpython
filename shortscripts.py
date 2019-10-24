#-- Factorising numbers
import primefac

print("Give an integer: ")
num = int(input())
out = list(primefac.primefac(num))
print("The factors are: ", out)

#-- Increase dimensionality of array
x[np.newaxis,:]
# or
x[:,np.newaxis]

#-- Tile arrays (replicate matrices)
np.tile(x[np.newaxis,:],(2,1))

#-- Definitions for nice plots
def cm2inch(value):
    return value/2.54

def set_size(w,h, ax=None):
    """ w, h: width, height in inches """
    if not ax: ax=plt.gca()
    l = ax.figure.subplotpars.left
    r = ax.figure.subplotpars.right
    t = ax.figure.subplotpars.top
    b = ax.figure.subplotpars.bottom
    figw = float(w)/(r-l)
    figh = float(h)/(t-b)
    ax.figure.set_size_inches(figw, figh)
    
#-- Plot settings
if True:
    matplotlib.rcParams['axes.linewidth']           = 0.5
    matplotlib.rcParams['xtick.major.size']         = 3
    matplotlib.rcParams['xtick.major.width']        = 0.5
    matplotlib.rcParams['xtick.minor.size']         = 2
    matplotlib.rcParams['xtick.minor.width']        = 0.25
    matplotlib.rcParams['ytick.major.size']         = 3
    matplotlib.rcParams['ytick.major.width']        = 0.5
    matplotlib.rcParams['ytick.minor.size']         = 2
    matplotlib.rcParams['ytick.minor.width']        = 0.25

    matplotlib.rcParams['xtick.direction']          = 'in'
    matplotlib.rcParams['ytick.direction']          = 'in'

    matplotlib.rcParams['xtick.major.pad']          = 5
    matplotlib.rcParams['xtick.minor.pad']          = 5
    matplotlib.rcParams['ytick.major.pad']          = 3
    matplotlib.rcParams['ytick.minor.pad']          = 3

    matplotlib.rcParams['mathtext.default']         = 'regular'
    matplotlib.rcParams['font.size']                = 10
    # matplotlib.rcParams['label.size']               = 24

    matplotlib.rcParams['lines.markeredgewidth']    = 0.5
    matplotlib.rcParams['lines.markersize']         = 6.0
    matplotlib.rcParams['lines.linewidth']          = 0.75

    matplotlib.rcParams['text.usetex']              = 'True'
    matplotlib.rcParams['font.family']              = 'serif'
    matplotlib.rcParams['font.serif']               = 'Computer Modern Roman'

    matplotlib.rcParams['axes.facecolor']           = 'White'
    matplotlib.rcParams['figure.facecolor']         = 'None'
#-- End

#-- Define the shared axis
fig1,(ax11,ax12) = plt.subplots(1, 2, sharey=True, facecolor='w')

#-- Set the limits
for axes in [ax11,ax12]:
    axes.plot([0,1],[0,0],'k--',zorder=-15,linewidth=0.5)
    if axes == ax11:
        axes.set_xlim(0,0.145)
        axes.set_ylim(-0.2,0.2)
        axes.yaxis.set_major_locator(MultipleLocator(0.1))
        axes.yaxis.set_minor_locator(MultipleLocator(0.05))
        axes.spines['right'].set_visible(False)
        axes.yaxis.tick_left()
        axes.tick_params(labeltop='off')
    elif axes == ax12:
        axes.set_xlim(1.0-0.145,1.0)
        axes.set_ylim(-0.2,0.2)
        axes.yaxis.set_major_locator(MultipleLocator(0.1))
        axes.yaxis.set_minor_locator(MultipleLocator(0.05))
        axes.spines['left'].set_visible(False)
        axes.yaxis.tick_right()
        
#-- Now properly size the plots
width = cm2inch(4./5.*3.5)
height = cm2inch(3.5)

plt.figure(fig1.number)
# fig1.tight_layout()
plt.subplots_adjust(wspace=0.15)

#-- Now make diagonal lines
d = .015 # How big to make the diagonal lines in axes coordinates
#-- Arguments to pass plot, just so we don't keep repeating them
kwargs = dict(transform=ax11.transAxes, color='k', clip_on=False, solid_capstyle='round',linewidth=0.5)
ax11.plot((1-d,1+d),(-d,+d), **kwargs) # top-left diagonal
ax11.plot((1-d,1+d),(1-d,1+d), **kwargs) # bottom-left diagonal
kwargs.update(transform=ax12.transAxes) # switch to the bottom axes
ax12.plot((-d,d),(-d,+d), **kwargs) # top-right diagonal
ax12.plot((-d,d),(1-d,1+d), **kwargs) # bottom-right diagonal

#-- Now set plot dimensions
set_size(width,height)
plt.text(-0.5, 1.1,u"(\\textit{a})",
     horizontalalignment='center',
     verticalalignment='center',
     transform = ax11.transAxes)
# plt.text(-0.05, -0.2,u"$z$",
#       horizontalalignment='center',
#       verticalalignment='center',
#       transform = ax22.transAxes)
plt.text(-0.05, 1.1,u"$\\alpha=1\\times 10^{-3}$",
      horizontalalignment='center',
      verticalalignment='center',
      transform = ax22.transAxes)
fig1.savefig('pyfigs/figure.pdf', format='pdf', bbox_inches='tight')
