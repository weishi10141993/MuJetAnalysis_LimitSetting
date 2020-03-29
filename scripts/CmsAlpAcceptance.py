#####################################################
#               13 TeV - year 2017
#####################################################
# (m_ALP) : (full acceptance after all selections)
CmsAlpAcceptance_2017_13TeV = [
[0.5,  0.16],
[0.6,  0.153],
[0.7,  0.149],
[0.8,  0.147],
[0.9,  0.145],
[1.0,  0.141],
[2.0,  0.137],
[3.0,  0.134],
[4.0,  0.132],
[5.0,  0.129],
[6.0,  0.128],
[7.0,  0.128],
[8.0,  0.128],
[9.0,  0.129],
[10.0, 0.129],
[15.0, 0.131],
[20.0, 0.134],
[25.0, 0.139],
[30.0, 0.149],
]

#####################################################
#               13 TeV - year 2018: TO BE UPDATED
#####################################################
# (m_ALP) : (full acceptance after all selections)
CmsAlpAcceptance_2018_13TeV = [
[0.5,  0.16],
[0.6,  0.153],
[0.7,  0.149],
[0.8,  0.147],
[0.9,  0.145],
[1.0,  0.141],
[2.0,  0.137],
[3.0,  0.134],
[4.0,  0.132],
[5.0,  0.129],
[6.0,  0.128],
[7.0,  0.128],
[8.0,  0.128],
[9.0,  0.129],
[10.0, 0.129],
[15.0, 0.131],
[20.0, 0.134],
[25.0, 0.139],
[30.0, 0.149],
]

#general function to do extrapolate
def fCmsAlpAcceptance(m):
    if m >= 0.5 and m <= 30.:
        m_im1 = 0.5
        m_i   = 0.5
        for i in range(len(CmsAlpAcceptance_2017_13TeV)): #TO BE GERNERALIZED
            m_i   = CmsAlpAcceptance_2017_13TeV[i][0]
            lim_i = CmsAlpAcceptance_2017_13TeV[i][1]
            if m == m_i:
                return lim_i
            elif m > m_im1 and m < m_i:
                a = (lim_i - lim_im1) / (m_i - m_im1)
                b = (lim_im1*m_i - lim_i*m_im1) / (m_i - m_im1)
                lim = a*m+b
                return lim
            m_im1 = m_i
            lim_im1 = lim_i
    else:
        print "Warning! Mass if outside the range."
