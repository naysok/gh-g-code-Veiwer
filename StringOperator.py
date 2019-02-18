import rhinoscriptsyntax as rs


ptX = []
ptY = []
ptZ = []
ptF = []
ptE = []

pts = []


for i in xrange(len(txt)):

    tmp_str = txt[i]

    boolX = "X" in tmp_str
    boolY = "Y" in tmp_str
    boolZ = "Z" in tmp_str
    boolF = "F" in tmp_str

    if boolX and boolY and boolZ and boolF:

        tmp_split_X = tmp_str.split("X")
        tmp_split_Y = tmp_split_X[1].split("Y")
        tmp_split_Z = tmp_split_Y[1].split("Z")
        tmp_split_F = tmp_split_Z[1].split("F")
        tmp_split_E = tmp_split_F[1].split("E")

        tmp_ptX = tmp_split_Y[0]
        tmp_ptY = tmp_split_Z[0]
        tmp_ptZ = tmp_split_F[0]
        tmp_ptF = tmp_split_E[0]
        tmp_ptE = tmp_split_E[1]


        tmp_pt = rs.AddPoint((tmp_ptX, tmp_ptY, tmp_ptZ))
        pts.append(tmp_pt)


        # ptX.append(tmp_ptX)
        # ptY.append(tmp_ptY)
        # ptZ.append(tmp_ptZ)
        ptF.append(tmp_ptF)
        # ptE.append(tmp_ptE)
