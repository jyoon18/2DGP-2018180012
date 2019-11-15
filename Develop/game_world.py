# Layer 0: 배경 오브젝트
# Layer 1: 앞에 있는 오브젝트들??

objects = [[], []]          # 게임 월드에 담겨있는 모든 객체들을 담고있는 리스트,
                            # Drawing Layer에 따라서 분류

def add_object(o, layer):
    objects[layer].append(o)        # 게임월드에 객체를 추가

def add_objects(l, layer):
    objects[layer] += l

def remove_object(o):
    for i in range(len(objects)):   # 게임 월드의 객체 제거
        if o in objects[i]:
            objects[i].remove(o)
            del o
            break

def clear():
    global objects
    #for i in range(len(objects)):   # 게임 월드 모든 객체가 제거
    #    for o in all_objects():
    #        remove_object(o)
    #        del o
    for o in all_objects():
        del o
    objects.clear()
    objects = [[], []]


def all_objects():
    for i in range(len(objects)): # 게임 월드의 모든 객체들을 하나씩 꺼내오기
        for o in objects[i]:
            yield o

