import numpy as np
import matplotlib.pyplot as plt

from anim import make_3d_animation

# Physical values are defined globally
dim = 3
L = 10 # length of box
m = 1 # mass of particles


def build_matrices(n_timesteps, n_particles):
    vel = np.zeros(shape=(Nt, N_particle, dim), dtype=float)
    pos = np.zeros(shape=(Nt, N_particle, dim), dtype=float)
    dis = np.zeros(Nt)
    F = np.zeros(shape=(Nt, N_particle, dim), dtype=float)
    return(vel,pos,dis,F)


def initial_state(N_particles, vel,pos):
    vel[0] = np.random.rand(N_particles, dim) * L
    pos[0] = np.random.rand(N_particles, dim) * L
    return(vel,pos)


def calculate_time_evolution(Nt, N_particle, vel, pos, dis):
    # distance = squareroot((dx)^2 + (dy)^2 + (dz)^2)
    dis[0] = (sum(pos[0,0,:] - pos[0,1,:])**2)**0.5 
    
    for v in range(1,Nt):        
        # velocity = vel[t-1] + 1/m * h * F[t-1]
        vel[v,:,:] = vel[v-1,:,:]+(1/m)*(1/Nt)#*F[v,i,:]

        
        pos[v] = (pos[v-1]+(1/Nt)*vel[v-1]) % L

        # distance = squareroot((dx)^2 + (dy)^2 + (dz)^2) 
        dis[v] = sum(pos[v,0,:] - pos[v,1,:])
    return(vel,pos,dis)


if __name__ == "__main__":    
    N_particle = 2
    Nt = 200 # number of timesteps  
    time = np.linspace(1,Nt,Nt)

    vel,pos,dis,F = build_matrices(Nt, N_particle)
    vel,pos = initial_state(N_particle,vel,pos)
    vel,pos,dis = calculate_time_evolution(Nt, N_particle, vel, pos, dis)    
    
    anim = make_3d_animation(L, pos, delay=30, rotate_on_play=0)
    plt.figure()
    plt.plot(time,pos[:,0,0]) 

    plt.show()


