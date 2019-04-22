class Solution:
    # @param A: Given an integer array
    # @return: void
    def heapify(self, A):
        # write your code here
        for i in xrange((len(A) - 1) / 2, -1, -1):
            while i < len(A):
                left, right = i * 2 + 1, i * 2 + 2
                min_pos = i #设最小值为父节点
                if (left < len(A)) and (A[left] < A[min_pos]):
                    #如果左节点的值小于父节点的值，则把左节点的index设为最小值的index
                    min_pos = left
                if (right < len(A)) and (A[right] < A[min_pos]):
                    #对于右节点，执行和左节点一样的操作
                    min_pos = right
                if min_pos != i:
                    #如果最小值的坐标和i不想等，则将最小值和I位置上的值互换
                    A[i], A[min_pos] = A[min_pos], A[i]
                    i = min_pos
                else:
                    break

# http://lintcode.com/zh-cn/problem/heapify/
