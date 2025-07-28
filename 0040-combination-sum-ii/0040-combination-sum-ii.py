class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        result = []
        def combination(index, choosen, sumi):
            if sumi == target:
                result.append(choosen[::])
                return 

            if index == len(candidates) or sumi > target:
                return

            choosen.append(candidates[index])
            combination(index + 1, choosen, sumi + candidates[index])
            choosen.pop()

            for i in range(index + 1, len(candidates)):
                if candidates[i - 1] != candidates[i]:
                    combination(i, choosen, sumi)
                    return

        combination(0, [], 0)
        return result

            
            