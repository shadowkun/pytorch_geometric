from __future__ import division


class NormalizeScale(object):
    def __call__(self, data):
        pos = data.pos
        pos = pos - pos.min(dim=0)[0]
        pos /= pos.max()
        data.pos = pos*0.9999
        return data
