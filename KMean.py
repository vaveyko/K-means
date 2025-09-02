import numpy as np
import matplotlib.pyplot as plt
from usefull import distance, is_equal, DotsClass
from MaxiMin import MaxiMin

"""
1) Глобальные переменные
2) 32, 42 строка

"""




class KMean:

    def __init__(self, dot_count, class_count, is_normal_generation=False, is_maximin_use=False):

        x_arr = np.array([])
        y_arr = np.array([])
        if is_normal_generation:
            for i in range(class_count):
                x = np.random.normal(np.random.randint(10, 90), np.random.randint(5, 10), int(dot_count/class_count))
                y = np.random.normal(np.random.randint(10, 90), np.random.randint(5, 10), int(dot_count/class_count))
                x_arr = np.hstack((x_arr, x))
                y_arr = np.hstack((y_arr, y))
        else:
            x_arr = np.random.uniform(0, 100, dot_count)
            y_arr = np.random.uniform(0, 100, dot_count)
        self.dots = np.stack((x_arr, y_arr), axis=1)

        # change
        array = []
        if is_maximin_use:
            maximin = MaxiMin(self.dots)
            array = maximin.get_start_kernel()
        else:
            kernels_index = np.random.choice(np.arange(0, len(self.dots)), size=class_count, replace=False)
            kernel_coord = np.array([self.dots[kernels_index[i]] for i in range(len(kernels_index))])

            for i in range(class_count):
                # поменять
                aboba = DotsClass(kernel_coord[i])
                array.append(aboba)

        self.classes_arr = array

        self.iteration()

    def iteration(self):
        for i in range(len(self.classes_arr)):
            self.classes_arr[i].clear_dot()

        for i in range(len(self.dots)):
            min_distance_kernel = 1_000_000_000
            kernel_ind = 0
            for j in range(len(self.classes_arr)):
                new_distance = distance(self.dots[i], self.classes_arr[j].get_kernel())
                if min_distance_kernel >= new_distance:
                    min_distance_kernel = new_distance
                    kernel_ind = j
            self.classes_arr[kernel_ind].add_dot(self.dots[i])

    def k_mean(self):
        is_changed = self._set_new_center()
        while is_changed:
            self.iteration()
            is_changed = self._set_new_center()
        self.show_plot("Конечный результат")

    def _set_new_center(self):
        is_changed = False
        for k in range(len(self.classes_arr)):
            dot_class: DotsClass = self.classes_arr[k]

            dots = dot_class.get_dots()
            x_coord = dots[:, 0].sum() / len(dots)
            y_coord = dots[:, 1].sum() / len(dots)
            old_kernel = dot_class.get_kernel()
            if not is_equal(old_kernel[0], x_coord) or not is_equal(old_kernel[1], y_coord):
                is_changed = True
            dot_class.set_kernel([x_coord, y_coord])

            self.classes_arr[k] = dot_class
        return is_changed

    def show_plot(self, title):
        fig, axes = plt.subplots(1, 1)
        fig.canvas.manager.set_window_title(title=title)
        for i in range(len(self.classes_arr)):
            dots = self.classes_arr[i].get_dots()
            axes.scatter(dots[:, 0], dots[:, 1])
        kernel_x = [self.classes_arr[i].get_kernel()[0] for i in range(len(self.classes_arr))]
        kernel_y = [self.classes_arr[i].get_kernel()[1] for i in range(len(self.classes_arr))]
        axes.scatter(kernel_x, kernel_y, c='black')
        fig.show()
