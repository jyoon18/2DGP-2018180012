# Layer 0: 배경 오브젝트
# Layer 1: 앞에 있는 오브젝트들??

objects = [[], []]          # 게임 월드에 담겨있는 모든 객체들을 담고있는 리스트,
                            # Drawing Layer에 따라서 분류

def add_object(o, layer):
    objects[layer].append(o)        # 게임월드에 객체를 추가

def add_objects(l, layer):
    objects[layer] += 1             # 게임월드에 객체들을 추가
