"""create table

Revision ID: a7126e21f479
Revises: 
Create Date: 2020-06-21 20:46:07.015441

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a7126e21f479'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('gejala',
    sa.Column('id', sa.BigInteger(), autoincrement=True, nullable=False),
    sa.Column('gejala', sa.String(length=200), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_gejala_created_at'), 'gejala', ['created_at'], unique=False)
    op.create_index(op.f('ix_gejala_updated_at'), 'gejala', ['updated_at'], unique=False)
    op.create_table('penyakit',
    sa.Column('id', sa.BigInteger(), autoincrement=True, nullable=False),
    sa.Column('penyakit', sa.String(length=140), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_penyakit_created_at'), 'penyakit', ['created_at'], unique=False)
    op.create_index(op.f('ix_penyakit_updated_at'), 'penyakit', ['updated_at'], unique=False)
    op.create_table('penyakitgejala',
    sa.Column('penyakit_id', sa.BigInteger(), nullable=True),
    sa.Column('gejala_id', sa.BigInteger(), nullable=True),
    sa.ForeignKeyConstraint(['gejala_id'], ['gejala.id'], ),
    sa.ForeignKeyConstraint(['penyakit_id'], ['penyakit.id'], )
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('penyakitgejala')
    op.drop_index(op.f('ix_penyakit_updated_at'), table_name='penyakit')
    op.drop_index(op.f('ix_penyakit_created_at'), table_name='penyakit')
    op.drop_table('penyakit')
    op.drop_index(op.f('ix_gejala_updated_at'), table_name='gejala')
    op.drop_index(op.f('ix_gejala_created_at'), table_name='gejala')
    op.drop_table('gejala')
    # ### end Alembic commands ###
