class Solution:
    def simplifyPath(self, path: str) -> str:
        paths = path.split('/')
        stack = []
        paths = list(filter(None, paths))
        for i in range(len(paths)):
            if paths[i] == '.':
                continue
            elif paths[i] == '..':
                if stack:
                    stack.pop()
            else:
                stack.append(paths[i])
        return '/'+'/'.join(stack)
