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

## 14.2
Let $G$ be any group.

(a) The subset $Z(G)$ of $G$ consisting of those $g \in G$ that commute with all other elements of the group is called the _centre_ of the group. Show that $Z(G)$ is a subgroup of $G$.

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