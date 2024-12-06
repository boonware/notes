# 14. Groups and Group Representations

## 14.1

Let $H_1$, $H_2$ be two subgroups of a group $G$. Show that $H_1 \cap H_2$ is also a subgroup.

### Solution

$$
    e \in H_1, e \in H_2 \implies e \in H_1 \cap H_2 \quad \text{(Identity)}
$$ 


$$
    \forall g \in H_1 \cap H_2 \implies g \in H_1, g \in H_2 \implies g^{-1} \in H_1, g^{-1} \in H_2 \implies g^{-1} \in H_1 \cap H_2 \quad \text{(Inverses)}
$$

$$
    \forall g, k \in H_1 \cap H_2 \implies g \in H_1, g \in H_2, k \in H_1, k \in H_2 \implies gk \in H_1, gk \in H_2 \implies gk \in H_1 \cap H_2 \quad \text{(Closure)}
$$

## 14.2 (a)
Let $G$ be any group.

The subset $Z(G)$ of $G$ consisting of those $g \in G$ that commute with all other elements of the group is called the _centre_ of the group. Show that $Z(G)$ is a subgroup of $G$.

### Solution

$$
    \forall g \in G, eg = ge \implies e \in Z(G) \quad \text{(Identity)}
$$

$$
    \exists g \in G \enspace | \enspace gk = kg \enspace \forall k \in G \implies g^{-1}gkg^{-1} = g^{-1}kgg^{-1} \iff kg^{-1} = g^{-1}k \iff g^{-1} \in Z(G) \quad \text{(Inverses)}
$$

$$
    \exists g, k \in G \enspace | \enspace gc = cg, kc = ck \enspace \forall c \in G \implies gkc = gck \iff gkc = cgk \iff gk \in Z(G) \quad \text{(Closure)}
$$

## 14.2 (b)
If $g$ is an element of $G$, the set $C_G(g)$ of elements of $G$ that commute with $g$ is called the _centralizer_ of $g$ in $G$. Show that it is a subgroup of $G$.

### Solution

$$
    \forall g \in G, \enspace eg = ge \implies e \in C_G(g) \quad \text{(Identity)}
$$

$$
    \forall g \in G, \enspace gg^{-1} = g^{-1}g \iff g^{-1} \in C_G(g) \quad \text{(Inverses)}
$$

$$
    \exists g, k \in G \enspace | \enspace gk = kg \implies g(gk) = g(kg) \iff g(gk) = (gk)g \iff gk \in C_G(g) \quad \text{(Closure)}
$$

## 14.2 (c)
If $H$ is a subgroup of G, the set of elements of $G$ that commute with all elements of $H$ is the _centralizer_ $C_G(H)$ of $H$ in $G$. Show that it is a subgroup of $G$.

### Solution

$$
    \forall g \in H, \enspace eg = ge \implies e \in C_G(H) \quad \text{(Identity)}
$$

$$
    \forall g \in H, \enspace gg^{-1} = g^{-1}g \iff g^{-1} \in C_G(H) \quad \text{(Inverses)}
$$

$$
    \exists g, k \in G, h \in H \enspace | \enspace gh = hg, \enspace kh = hk \implies kgh = khg \iff (kg)h = h(kg) \iff gk \in C_G(H) \quad \text{(Closure)}
$$

## 14.2 (d)
If $H$ is a subgroup of $G$, the set $N_G(H) \subset G$ consisting of those $g$ such that $g^{-1}Hg = H$ is called the _normalizer_ of $H$ in $G$. Show that $N_G(H)$ is a
subgroup of $G$, and that $H$ is a normal subgroup of $N_G(H)$.

### Solution (Part 1)

$$
    \forall h \in H, \enspace e^{-1}he = h \implies e \in N_G(H) \quad \text{(Identity)}
$$

$$
    \exists g \in G \enspace | \enspace \forall h \in H, \enspace g^{-1}hg = h \implies gg^{-1}hgg^{-1} = ghg^{-1} \iff h = ghg^{-1} \iff g^{-1} \in N_G(H) \quad \text{(Inverses)}
$$

$$
    \exists g, k \in G \enspace | \enspace \forall h \in H, \enspace g^{-1}hg = h, \enspace k^{-1}hk = h \implies g^{-1}k^{-1}hkg = h, \iff (kg)^{-1}hkg = h \iff kg \in N_G(H) \quad \text{(Closure)}
$$

TODO show abelian, both products exist