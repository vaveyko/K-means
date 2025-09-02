import numpy as np
from usefull import distance, DotsClass


def find_max_remote(dots, kernel):
    most_remote = dots[0]
    most_remote_distance = distance(most_remote, kernel)
    for dot in dots:
        cur_distance = distance(kernel, dot)
        if cur_distance > most_remote_distance:
            most_remote_distance = cur_distance
            most_remote = dot
    return most_remote


class MaxiMin:

    def __init__(self, dots):
        self.dots = dots
        self.start_point = dots[np.random.randint(len(dots))]
        self.classes_arr = [DotsClass(self.start_point)]

    def find_new_kernel(self):
        new_kernels = []
        for i in range(len(self.classes_arr)):
            kernel = self.classes_arr[i].get_kernel()
            dots = self.classes_arr[i].get_dots()
            max_dot = find_max_remote(dots, kernel)
            new_kernels.append([max_dot, distance(max_dot, kernel)]) # [[x, y], distance]
        max_dot_index = 0
        for i in range(len(new_kernels)):
            if new_kernels[i][1] > new_kernels[max_dot_index][1]:
                max_dot_index = i
        return new_kernels[max_dot_index][1], new_kernels[max_dot_index][0]

    def get_start_kernel(self):
        while True:
            self.__paint_dots()
            cur_distance, new_dot = self.find_new_kernel()
            cur_sum = 0
            count = 0
            for i in range(len(self.classes_arr)):
                for j in range(i+1, len(self.classes_arr)):
                    cur_sum += distance(self.classes_arr[i].get_kernel(), self.classes_arr[j].get_kernel())
                    count += 1
            average = cur_sum / count if count > 0 else 0
            if cur_distance > average/2:
                self.classes_arr.append(DotsClass(new_dot))
            else:
                break
        return self.classes_arr

    def __paint_dots(self):
        for classes in self.classes_arr:
            classes.clear_dot()
        for dot in self.dots:
            class_ind = 0
            min_distance = distance(dot, self.classes_arr[class_ind].get_kernel())
            for i in range(len(self.classes_arr)):
                dot_class = self.classes_arr[i]
                curr_distance = distance(dot, dot_class.get_kernel())
                if curr_distance < min_distance:
                    min_distance = curr_distance
                    class_ind = i
            self.classes_arr[class_ind].add_dot(dot)
