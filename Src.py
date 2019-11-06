import matplotlib.pyplot as plt

class Src():
    """Contains functions to allow importing from one notebook to another"""
    def __init__(self):
        pass
    
    def plot_results(acc, val_acc, fig_no):
        """Plot the model history results, returns the results as a tuple"""
        # Plot train vs test accuracy per epoch
        plt.figure()

        # Use the history metrics
        plt.plot(acc)
        plt.plot(val_acc)

        # add some labels
        plt.title('Model accuracy')
        plt.ylabel('Accuracy')
        plt.xlabel('Epoch')
        plt.legend(['Training data', 'Validation data'])
        plt.ylim(0, 1)  # set to highest possible value to

        # the highest accuracy score
        print('\n Fig {}. The highest validation score:{:.3f} | The highest training score {:.3f}'.format(
            fig_no, max(val_acc), max(acc)))
        plt.show()
        # keep a record of the results
        return (max(acc), max(val_acc))
        